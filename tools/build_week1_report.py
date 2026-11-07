"""Build the week 1 report from Markdown. Run from the repository root."""

from html import escape
from pathlib import Path
import math
import re

from PIL import Image as PILImage, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image, KeepTogether, PageBreak, Paragraph, Preformatted,
    SimpleDocTemplate, Spacer, Table, TableStyle,
)

REPORT_DIR = Path("week1") / "reports"
FIGURES = REPORT_DIR / "figures"
FONTS = Path("assets") / "fonts"
REGULAR = FONTS / "NanumGothic-Regular.ttf"
BOLD = FONTS / "NanumGothic-Bold.ttf"
SOURCE = REPORT_DIR / "team16_week1.md"
OUTPUT = REPORT_DIR / "team16_week1.pdf"
INK = "#172C40"
BLUE = "#1A657A"
TEAL = "#087F83"
PALE = "#F2F6F8"


def pil_font(size, bold=False):
    return ImageFont.truetype(str(BOLD if bold else REGULAR), size)


def arrow(draw, start, end, fill=BLUE, width=4):
    draw.line([start, end], fill=fill, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    tip = [end]
    for delta in (-0.52, 0.52):
        tip.append((end[0] - 14 * math.cos(angle + delta),
                    end[1] - 14 * math.sin(angle + delta)))
    draw.polygon(tip, fill=fill)


def make_figures():
    FIGURES.mkdir(parents=True, exist_ok=True)
    image = PILImage.new("RGB", (1400, 490), "white")
    draw = ImageDraw.Draw(image)
    for left, title in [(10, "PRM: 로드맵"), (715, "RRT: 트리 확장")]:
        draw.rounded_rectangle((left, 8, left + 675, 475), 18,
                               fill=PALE, outline="#D6E0E5", width=2)
        draw.text((left + 24, 26), title, font=pil_font(29, True), fill=INK)
        draw.rectangle((left + 272, 160, left + 384, 335), fill="#B4C2CC")
        draw.text((left + 279, 225), "장애물", font=pil_font(23), fill=INK)
    nodes = [(64, 320), (170, 265), (205, 123), (345, 102),
             (469, 127), (540, 246), (614, 340), (444, 395), (210, 402)]
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
             (6, 7), (7, 8), (8, 0), (1, 8)]
    for a, b in edges:
        draw.line([nodes[a], nodes[b]], fill=BLUE, width=5)
    for x, y in nodes:
        draw.ellipse((x - 9, y - 9, x + 9, y + 9), fill=BLUE)
    draw.text((35, 437), "자유 공간의 표본을 연결", font=pil_font(22), fill=INK)
    root = (770, 350)
    branches = [(root, (850, 280)), ((850, 280), (900, 190)),
                ((900, 190), (960, 125)), ((960, 125), (1070, 106)),
                ((1070, 106), (1180, 140)), ((1180, 140), (1260, 205)),
                ((850, 280), (860, 385)), ((860, 385), (980, 410)),
                ((900, 190), (818, 120))]
    for a, b in branches:
        draw.line([a, b], fill=TEAL, width=5)
        for x, y in (a, b):
            draw.ellipse((x - 7, y - 7, x + 7, y + 7), fill=TEAL)
    draw.ellipse((root[0] - 12, root[1] - 12, root[0] + 12, root[1] + 12), fill=INK)
    draw.text((740, 368), "시작", font=pil_font(22), fill=INK)
    arrow(draw, (1260, 205), (1338, 279), fill=TEAL)
    draw.ellipse((1345, 289, 1361, 305), outline=TEAL, width=3)
    draw.text((1168, 330), "새 표본 방향", font=pil_font(22), fill=INK)
    draw.text((740, 437), "시작점에서 점진적으로 확장", font=pil_font(22), fill=INK)
    image.save(FIGURES / "planning_concepts.png")

    image = PILImage.new("RGB", (1400, 340), "white")
    draw = ImageDraw.Draw(image)
    draw.text((25, 12), "정규화된 가중치", font=pil_font(27, True), fill=INK)
    draw.text((835, 12), "재표본화 후 (한 가지 예)", font=pil_font(27, True), fill=INK)
    for i, (weight, y) in enumerate(zip([0.1, 0.2, 0.6, 0.1], [85, 150, 215, 280]), 1):
        draw.text((30, y - 10), f"x{i}", font=pil_font(23), fill=INK)
        draw.rounded_rectangle((85, y - 12, 85 + int(650 * weight), y + 17), 5, fill=BLUE)
        draw.text((505, y - 10), f"{weight:.1f}", font=pil_font(23), fill=INK)
    arrow(draw, (610, 165), (770, 165))
    for label, y in zip(["x1", "x2", "x3", "x3"], [85, 150, 215, 280]):
        draw.rounded_rectangle((835, y - 16, 1330, y + 25), 9, fill=PALE)
        draw.text((865, y - 10), label, font=pil_font(23, True), fill=TEAL)
        draw.text((1070, y - 10), "가중치 1/4", font=pil_font(23), fill=INK)
    image.save(FIGURES / "particle_resampling.png")

    image = PILImage.new("RGB", (1400, 320), "white")
    draw = ImageDraw.Draw(image)
    draw.text((24, 15), "한 광선의 유효 반사 관측", font=pil_font(27, True), fill=INK)
    fills = ["#A9DEDC"] * 5 + ["#244C64"] + ["#E2E7EB"] * 4
    for i, fill in enumerate(fills):
        x = 210 + i * 108
        draw.rectangle((x, 90, x + 104, 190), fill=fill, outline="white", width=3)
    draw.ellipse((45, 115, 100, 170), fill=TEAL)
    draw.text((32, 191), "센서", font=pil_font(24), fill=INK)
    arrow(draw, (100, 141), (795, 141), fill="#AA5B21", width=5)
    draw.text((280, 223), "통과: 비점유 증거", font=pil_font(25), fill=INK)
    draw.text((712, 223), "반사점: 점유 증거", font=pil_font(25), fill=INK)
    draw.text((1080, 223), "뒤쪽: 미관측", font=pil_font(25), fill=INK)
    image.save(FIGURES / "occupancy_ray.png")


def markup(text):
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    return re.sub(r"`([^`]+)`", r"\1", text)


def build_report():
    for path in (REGULAR, BOLD, SOURCE):
        if not path.is_file():
            raise FileNotFoundError(f"Missing relative project file: {path}")
    pdfmetrics.registerFont(TTFont("Nanum", str(REGULAR)))
    pdfmetrics.registerFont(TTFont("NanumBold", str(BOLD)))
    pdfmetrics.registerFontFamily("Nanum", normal="Nanum", bold="NanumBold")
    make_figures()
    body = ParagraphStyle("body", fontName="Nanum", fontSize=10,
                          leading=15.6, textColor=colors.HexColor(INK),
                          wordWrap="CJK", spaceAfter=9)
    styles = {
        "body": body,
        "title": ParagraphStyle("title", parent=body, fontName="NanumBold",
                                fontSize=21, leading=28, spaceAfter=12),
        "h2": ParagraphStyle("h2", parent=body, fontName="NanumBold",
                             fontSize=15, leading=21, spaceBefore=8, spaceAfter=12,
                             keepWithNext=True),
        "h3": ParagraphStyle("h3", parent=body, fontName="NanumBold",
                             fontSize=11, leading=17, spaceBefore=8, spaceAfter=7,
                             keepWithNext=True),
        "cell": ParagraphStyle("cell", parent=body, fontSize=9.3, leading=14,
                               spaceAfter=0),
        "caption": ParagraphStyle("caption", parent=body, fontSize=8.3,
                                  leading=12, textColor=colors.HexColor("#516676"),
                                  spaceAfter=12),
        "code": ParagraphStyle("code", fontName="Courier", fontSize=8.3,
                               leading=11.8, spaceBefore=3, spaceAfter=12,
                               leftIndent=9, backColor=colors.HexColor(PALE),
                               borderPadding=8),
        "url": ParagraphStyle("url", parent=body, fontSize=8.4, leading=12,
                              textColor=colors.HexColor(BLUE), spaceAfter=8),
    }
    page_width, _ = A4
    content_width = page_width - 104
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    story = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line == "<!-- pagebreak -->":
            story.append(PageBreak())
            i += 1
            continue
        if line.startswith("```"):
            code = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i])
                i += 1
            story.append(Preformatted("\n".join(code), styles["code"]))
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [cell.strip() for cell in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", cell.replace(" ", "")) for cell in cells):
                    rows.append([Paragraph(markup(cell), styles["cell"]) for cell in cells])
                i += 1
            n = len(rows[0])
            widths = [content_width * 0.23, content_width * 0.77] if n == 2 else [content_width / n] * n
            table = Table(rows, colWidths=widths, repeatRows=1, hAlign="LEFT")
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E4EEF2")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7F9FA")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("LINEBELOW", (0, 0), (-1, 0), 0.6, colors.HexColor("#BBCDD6")),
            ]))
            story.extend([table, Spacer(1, 11)])
            continue
        match = re.fullmatch(r"!\[(.+)\]\((.+)\)", line)
        if match:
            caption, relpath = match.groups()
            path = REPORT_DIR / Path(relpath)
            with PILImage.open(path) as picture:
                width, height = picture.size
            image = Image(str(path), width=content_width,
                          height=content_width * height / width)
            story.append(KeepTogether([image, Spacer(1, 5), Paragraph(markup(caption), styles["caption"])]))
            i += 1
            continue
        if line.startswith("### "):
            story.append(Paragraph(markup(line[4:]), styles["h3"]))
        elif line.startswith("## "):
            story.append(Paragraph(markup(line[3:]), styles["h2"]))
        elif line.startswith("# "):
            story.append(Paragraph(markup(line[2:]), styles["title"]))
        elif line.startswith("https://"):
            url = escape(line, quote=True)
            story.append(Paragraph(f'<link href="{url}">{url}</link>', styles["url"]))
        else:
            story.append(Paragraph(markup(line), styles["body"]))
        i += 1

    def decorate(canvas, doc):
        width, height = A4
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#CDD9E0"))
        canvas.setLineWidth(0.6)
        canvas.line(52, height - 36, width - 52, height - 36)
        canvas.line(52, 37, width - 52, 37)
        canvas.setFont("Nanum", 8)
        canvas.setFillColor(colors.HexColor("#526878"))
        canvas.drawString(52, height - 27, "SWE4007 | GPS Localization | Week 1")
        canvas.drawString(52, 24, "16번 개인 | 2021245017 공지혁")
        canvas.drawRightString(width - 52, 24, str(doc.page))
        canvas.restoreState()

    doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=52,
                            leftMargin=52, topMargin=51, bottomMargin=52,
                            title="16번 개인 공지혁 - 로봇 알고리즘 1주차 보고서",
                            author="공지혁", subject="GPS Localization Week 1")
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
    print(f"Built: {OUTPUT}")


if __name__ == "__main__":
    build_report()
