#!/usr/bin/env python3
"""Render the 22 November 2026 world-news broadsheet (1024x1024 PNG).

Written fresh for news-image-20261122. All facts were verified against
sources read on 22 Nov 2026 (see BUILD_NOTES.md); nothing is invented.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
CREAM = (248, 243, 230)
NAVY = (16, 38, 74)
NAVY_LIGHT = (32, 64, 110)
RED = (176, 30, 36)
GREY = (90, 88, 80)
INK = (24, 24, 22)
RULE = (16, 38, 74)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap measured with the real font."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    mx = 40  # side margin
    cw = W - 2 * mx  # content width = 944

    # --- masthead ------------------------------------------------------
    y = 16
    d.rectangle([0, 0, W, 6], fill=NAVY)
    f_mast = font(SERIF_B, 68)
    d.text((W // 2, y), "THE WORLD TODAY", font=f_mast, fill=NAVY, anchor="ma")
    y = 96
    f_date = font(SANS_B, 21)
    d.text((W // 2, y), "SUNDAY, 22 NOVEMBER 2026  ·  MORNING EDITION",
           font=f_date, fill=NAVY, anchor="ma")
    y = 128
    d.line([(mx, y), (W - mx, y)], fill=RULE, width=3)
    d.line([(mx, y + 6), (W - mx, y + 6)], fill=RULE, width=1)
    y = 142

    # --- breaking banner ----------------------------------------------
    d.rectangle([mx, y, W - mx, y + 38], fill=RED)
    f_ban = font(SANS_B, 22)
    d.text((W // 2, y + 19), "BREAKING NEWS  —  GULF CRISIS DEEPENS",
           font=f_ban, fill=(255, 255, 255), anchor="mm")
    y += 52

    # --- lead story ----------------------------------------------------
    f_kick = font(SANS_B, 18)
    d.text((mx, y), "MIDDLE EAST  •  IRAN STRIKES U.S. BASES IN BAHRAIN",
           font=f_kick, fill=RED)
    y += 26
    f_head = font(SERIF_B, 34)
    lead_head = ("Iran claims missile and drone strikes "
                 "on U.S. Patriot radars in Bahrain")
    y = draw_lines(d, wrap(d, lead_head, f_head, cw), mx, y, f_head, NAVY, 40)
    y += 6
    f_body = font(SERIF, 20)
    lead_body = (
        "Iran's Revolutionary Guard said late on Saturday it fired missiles "
        "and drones at two U.S. Patriot air-defence radars at the al-Riffa "
        "and Awali bases in Bahrain, in retaliation for alleged U.S. drone "
        "incursions into Iranian airspace. Bahrain said the attack instead "
        "hit a civilian industrial facility, starting a fire but causing no "
        "casualties. Washington has not confirmed any damage to its bases, "
        "which host the U.S. Navy's Fifth Fleet, in the latest flare-up of "
        "a widening Gulf confrontation."
    )
    y = draw_lines(d, wrap(d, lead_body, f_body, cw), mx, y, f_body, INK, 26)
    y += 12
    d.line([(mx, y), (W - mx, y)], fill=RULE, width=2)
    y += 14

    # --- 2x2 grid ------------------------------------------------------
    grid = [
        ("UKRAINE",
         "Russia fires about 550 drones and missiles at Ukraine overnight",
         "President Volodymyr Zelenskyy said at least five people were "
         "killed and ten injured as Russia launched 496 drones and 53 "
         "missiles. A family of four died in Lapaivka, in the Lviv region, "
         "and strikes hit nine regions."),
        ("MEXICO",
         "Mexico captures \u201cEl Chapo Isidro\u201d, FBI most-wanted cartel boss",
         "Fausto Isidro Meza Flores was seized in Guasave, Sinaloa, on "
         "Friday night with U.S. intelligence help, officials said. Eleven "
         "people died in the fighting \u2014 seven suspected gunmen and four "
         "soldiers \u2014 and he was flown to Mexico City."),
        ("CLIMATE  •  COP31",
         "COP31 talks run into a second day of overtime in Antalya",
         "Nearly 200 nations remained deadlocked on Sunday over a draft deal "
         "that drops all mention of fossil fuels. The EU warned it would "
         "accept \u201ca good deal or no deal\u201d as a third draft was promised."),
        ("TRADE",
         "EU and Indonesia sign landmark trade deal after a decade of talks",
         "The pact signed in Brussels on Saturday will scrap tariffs on up "
         "to 98.5% of goods traded between the two sides. The EU says it "
         "will save exporters about \u20ac650 million a year in duties."),
    ]
    f_gkick = font(SANS_B, 16)
    f_ghead = font(SERIF_B, 23)
    f_gbody = font(SERIF, 16)
    gap = 24
    cell_w = (cw - gap) // 2
    cell_h = 186
    gx0, gy0 = mx, y
    for i, (kick, head, body) in enumerate(grid):
        cx = gx0 + (i % 2) * (cell_w + gap)
        cy = gy0 + (i // 2) * (cell_h + 14)
        d.text((cx, cy), kick, font=f_gkick, fill=RED)
        cy += 22
        cy = draw_lines(d, wrap(d, head, f_ghead, cell_w), cx, cy,
                        f_ghead, NAVY, 28)
        cy += 4
        draw_lines(d, wrap(d, body, f_gbody, cell_w), cx, cy,
                   f_gbody, INK, 20)
        if i % 2 == 0:
            d.line([(cx + cell_w + gap // 2, gy0 + (i // 2) * (cell_h + 14)),
                    (cx + cell_w + gap // 2,
                     gy0 + (i // 2) * (cell_h + 14) + cell_h)],
                   fill=(190, 180, 160), width=1)
    y = gy0 + 2 * cell_h + 14 + 6
    d.line([(mx, y), (W - mx, y)], fill=RULE, width=2)
    y += 12

    # --- also today strip ----------------------------------------------
    d.rectangle([mx, y, W - mx, y + 110], fill=NAVY)
    f_strip_h = font(SANS_B, 17)
    d.text((mx + 16, y + 12), "ALSO TODAY", font=f_strip_h, fill=(255, 214, 90))
    f_strip = font(SANS, 15)
    items = [
        "HONG KONG \u2014 Polls open: 856 candidates contest 723 seats on the "
        "Election Committee that picks the city's next leader.",
        "PERU \u2014 Magnitude 6.7 quake shakes the Andes near Carhuamayo; "
        "felt in Lima, no casualties or damage reported.",
        "MYANMAR \u2014 Magnitude 4.1 earthquake strikes in the early hours "
        "of Sunday, seismologists say.",
        "UNITED STATES \u2014 The FBI is reported to be investigating an "
        "apparent hack of its criminal database.",
    ]
    sy = y + 36
    for it in items:
        lines = wrap(d, it, f_strip, cw - 32)
        for ln in lines:
            d.text((mx + 16, sy), ln, font=f_strip, fill=(240, 238, 228))
            sy += 18
    y = y + 110 + 8
    print("strip top", y - 118, "footer y", y)

    # --- footer --------------------------------------------------------
    f_foot = font(SANS, 13)
    d.text((W // 2, y), "THE WORLD TODAY  ·  Sunday, 22 November 2026  ·  "
           "Sources: AP, Reuters, AFP, IRNA, European Commission  ·  All times GMT",
           font=f_foot, fill=GREY, anchor="ma")

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
