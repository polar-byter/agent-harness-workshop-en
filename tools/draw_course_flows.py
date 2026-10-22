"""Render data transfer and state changes in teaching examples."""
import argparse
import math
import runpy
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

WIDTH = 480
HEIGHT = 650
INK = '#21384c'
MUTED = '#587083'
GREEN = '#147c70'
BLUE = '#315bb0'
PALE = '#e6f3ef'
FONTS = Path('C:/Windows/Fonts')


def font(size=17, bold=False):
    return ImageFont.truetype(str(FONTS / ('segoeuib.ttf' if bold else 'segoeui.ttf')), size)


def paragraph(draw, text, position, width, size=17, color=INK, bold=False):
    """Wrap by words and reject text that does not fit its panel."""
    selected = font(size, bold)
    x, y = position
    for source_line in text.split('\n'):
        line = ''
        for word in source_line.split():
            assert draw.textlength(word, font=selected) <= width, word
            candidate = (line + ' ' + word).strip()
            if draw.textlength(candidate, font=selected) > width:
                draw.text((x, y), line, font=selected, fill=color)
                y += size + 6
                line = word
            else:
                line = candidate
        draw.text((x, y), line, font=selected, fill=color)
        y += size + 6
    return y


def panel(draw, box, heading, body, tint='white', size=17):
    left, top, right, bottom = box
    draw.rounded_rectangle(box, radius=12, fill=tint, outline='#cbd8e1', width=1)
    y = paragraph(draw, heading, (left + 14, top + 9), right - left - 28, 16, MUTED, True)
    y = paragraph(draw, body, (left + 14, y + 5), right - left - 28, size)
    assert y <= bottom - 4, (heading, body, y, bottom)


def arrow(draw, points, color=GREEN, width=3):
    draw.line(points, fill=color, width=width, joint='curve')
    x, y = points[-1]
    previous = points[-2]
    angle = math.atan2(y - previous[1], x - previous[0])
    draw.polygon([(x, y), (x - 10 * math.cos(angle - .5), y - 10 * math.sin(angle - .5)),
                  (x - 10 * math.cos(angle + .5), y - 10 * math.sin(angle + .5))], fill=color)


def point_on_route(points, fraction):
    lengths = [math.dist(a, b) for a, b in zip(points, points[1:])]
    remaining = sum(lengths) * fraction
    for a, b, length in zip(points, points[1:], lengths):
        if remaining <= length:
            ratio = remaining / length if length else 0
            return a[0] + ratio * (b[0] - a[0]), a[1] + ratio * (b[1] - a[1])
        remaining -= length
    return points[-1]


def packet(draw, points, fraction, label):
    x, y = point_on_route(points, fraction)
    if fraction >= 1:
        draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill=GREEN)
        return
    selected = font(14, True)
    width = draw.textlength(label, font=selected) + 20
    left = max(6, min(WIDTH - width - 6, x - width / 2))
    draw.rounded_rectangle((left, y - 14, left + width, y + 15), 7, fill=BLUE)
    draw.text((left + 10, y - 11), label, font=selected, fill='white')


def base(title, subtitle):
    picture = Image.new('RGB', (WIDTH, HEIGHT), '#f3f7fa')
    draw = ImageDraw.Draw(picture)
    y = paragraph(draw, title, (20, 12), 440, 23, INK, True)
    assert y <= 77, title
    paragraph(draw, subtitle, (20, 80), 440, 14, MUTED)
    draw.line((20, 109, 460, 109), fill='#ccd8e1')
    return picture, draw


def draw_transfer(story, index, progress):
    scene = story['scenes'][index]
    picture, draw = base(story['title'], 'Teaching example. Values are selected for explanation.')
    paragraph(draw, f'{index + 1}/{len(story["scenes"])}. ' + scene['action'], (20, 120), 440, 19, INK, True)
    panel(draw, (20, 185, 460, 330), scene['source'], scene['before'])
    route = [(240, 331), (240, 395)]
    arrow(draw, route)
    packet(draw, route, progress, scene['packet'])
    arrived = progress >= 1
    panel(draw, (20, 397, 460, 552), scene['destination'],
          scene['after'] if arrived else scene.get('waiting', 'The data has not arrived yet.'), PALE if arrived else 'white')
    y = paragraph(draw, scene['explanation'], (24, 568), 432, 16, MUTED)
    assert y <= 642, scene['explanation']
    return picture


def draw_summary(story):
    """The static alternative shows the route, not just the final frame."""
    picture, draw = base(story['title'], 'Overview of the same teaching example.')
    scenes = story['scenes']
    top = 122
    row_height = min(116, 490 // len(scenes))
    for index, scene in enumerate(scenes):
        draw.ellipse((20, top + 5, 45, top + 30), fill=GREEN)
        draw.text((27, top + 6), str(index + 1), font=font(15, True), fill='white')
        y = paragraph(draw, scene['action'], (57, top), 400, 17, INK, True)
        y = paragraph(draw, scene.get('summary', scene['after']), (57, y + 1), 400, 16, MUTED)
        assert y <= top + row_height, (story['title'], scene['action'], 'summary overflow')
        top += row_height
    return picture


LOOP_STEPS = [
    ('First model request', 'task = "Find the return clauses\n  in the policy"\nevents = []',
     'No result yet. Send the task and empty history.', [(240, 115), (240, 151)], 'task + []'),
    ('The model requested a search', 'command = {"type": "tool",\n  "tool": "find_notes", "query": "return"}',
     'This describes an action. The model does not open the file itself.', [(157, 181), (110, 181), (110, 266)], 'find_notes: return'),
    ('The program permits the operation', 'dispatch_tool(command, notes_path)\nTool: "find_notes". Query: "return".',
     'Check the name and call search on the selected source.', [(194, 296), (286, 296)], 'query: return'),
    ('Search returned source lines', 'result = {"matches": [\n  "Returns are accepted...",\n  "RETURNED money...",\n  "A receipt or order number..."]}',
     'The program receives the result before it is sent to the model.', [(370, 327), (370, 355), (240, 355)], '3 source lines'),
    ('Record the completed tool action', 'events.append({\n  "command": command, "result": result\n})\nHistory now contains one event.',
     'Keep the search command and its result together.', [(240, 355), (240, 386)], 'command + result'),
    ('Second model request', 'decide(task, events)\nThe same task + the search command\n+ the three returned clauses.',
     'Return to the model with the evidence obtained by the tool.', [(156, 414), (12, 414), (12, 181), (156, 181)], 'task + 1 event'),
    ('The model returned an answer', '{"type": "answer",\n "text": "Found three clauses\n  about returns."}',
     'run_agent returns completed. This example needs no further search.', [(324, 181), (468, 181), (468, 414), (324, 414)], 'final answer'),
]


def draw_cycle(index, progress):
    title, data, explanation, route, label = LOOP_STEPS[index]
    picture, draw = base('How the agent loop closes', 'An illustrative two-request route, not a recorded run.')
    actors = [((156, 151, 324, 212), 'Model', 'chooses an action'),
              ((26, 266, 194, 327), 'dispatch_tool', 'checks and calls'),
              ((286, 266, 454, 327), 'find_notes', 'searches source lines'),
              ((156, 386, 324, 447), 'run_agent', 'stores the event list')]
    arrow(draw, [(157, 181), (110, 181), (110, 266)], '#a7b8c4', 2)
    arrow(draw, [(194, 296), (286, 296)], '#a7b8c4', 2)
    arrow(draw, [(370, 327), (370, 355), (240, 355), (240, 386)], '#a7b8c4', 2)
    arrow(draw, [(156, 414), (12, 414), (12, 181), (156, 181)], '#a7b8c4', 2)
    for box, heading, detail in actors:
        panel(draw, box, heading, detail, size=12)
    draw.text((68, 225), '1. Command', font=font(14), fill=MUTED)
    draw.text((283, 350), '2. Result', font=font(14), fill=MUTED)
    draw.text((49, 358), '3. Next', font=font(13), fill=MUTED)
    draw.text((49, 375), 'request', font=font(13), fill=MUTED)
    arrow(draw, route)
    packet(draw, route, progress, label)
    has_event = index > 4 or (index == 4 and progress >= 1)
    draw.text((158, 223), 'events: ' + ('[1 event]' if has_event else '[]'), font=font(14, True), fill=GREEN)
    draw.text((158, 242), 'Model calls: ' + ('1' if index < 5 else '2'), font=font(14), fill=MUTED)
    if index == 6:
        draw.text((340, 223), 'Finish', font=font(13, True), fill=GREEN)
    y = paragraph(draw, f'{index + 1}/7. {title}', (20, 461), 440, 18, INK, True)
    y = paragraph(draw, data, (25, y + 5), 430, 16)
    y = paragraph(draw, explanation, (25, y + 6), 430, 14, MUTED)
    assert y <= 647, (title, y)
    return picture


def cycle_summary():
    story = {'title': 'Why this is a loop', 'scenes': [
        {'action': 'Send the task to the model', 'after': 'task + events=[] -> find_notes command'},
        {'action': 'The program executes the search', 'after': 'dispatch_tool -> find_notes -> three clauses'},
        {'action': 'Record the command and result', 'after': 'events.append({command, result})'},
        {'action': 'Ask the model again', 'after': 'The same task + history with the found clauses'},
        {'action': 'Answer or continue the exchange', 'after': 'type="answer" ends the run; max_steps bounds the number of decisions.'},
    ]}
    picture = draw_summary(story)
    draw = ImageDraw.Draw(picture)
    arrow(draw, [(47, 453), (10, 453), (10, 137), (19, 137)], BLUE, 2)
    return picture


def save_animation(destination, frames, durations):
    destination.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(destination, save_all=True, append_images=frames[1:], duration=durations,
                   loop=0, disposal=2, optimize=True)


def render(story, vault, review_folder):
    destination = vault / story['path']
    frames, durations, keyframes = [], [], []
    cycle = story.get('kind') == 'cycle'
    count = len(LOOP_STEPS) if cycle else len(story['scenes'])
    for index in range(count):
        for tick in range(10):
            progress = tick / 9
            frame = draw_cycle(index, progress) if cycle else draw_transfer(story, index, progress)
            frames.append(frame)
            durations.append(3000 if tick == 9 else (600 if tick == 0 else 70))
        keyframes.append(frames[-1])
    save_animation(destination, frames, durations)
    (cycle_summary() if cycle else draw_summary(story)).save(destination.with_suffix('.png'))
    if review_folder:
        review_folder.mkdir(parents=True, exist_ok=True)
        sheet = Image.new('RGB', (WIDTH * 3, HEIGHT * math.ceil(count / 3)), 'white')
        for index, frame in enumerate(keyframes):
            sheet.paste(frame, ((index % 3) * WIDTH, (index // 3) * HEIGHT))
        sheet.save(review_folder / (destination.stem + '.png'))
    print(destination.name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--vault', type=Path, required=True)
    parser.add_argument('--only', help='Part of a filename to render one diagram')
    parser.add_argument('--review-folder', type=Path)
    args = parser.parse_args()
    stories = runpy.run_path(str(Path(__file__).with_name('course_flow_examples.py')))['STORIES']
    for story in stories:
        if not args.only or args.only in story['path']:
            render(story, args.vault, args.review_folder)


if __name__ == '__main__':
    main()
