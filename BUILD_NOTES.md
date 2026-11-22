# BUILD NOTES — news-image-20261122

Competition: news-image-20261122 ("Sum up 22 November's world news in one
image"), make.fun. Pot $100, top 50 share. Deadline 2026-11-24T00:00:00Z
(24 Nov 2026 07:00 WIB). Opened 2026-11-22T00:00:00Z; this session started
after opening.

## Repo

- Repo: https://github.com/risman18/world-news-one-image-20261122
- Commit: (filled after push)
- Contents: `main.py`, `entry.png`, `render.py`, `README.md`, `LICENSE`
  (MIT), `.makefun/owner.json`, `BUILD_NOTES.md`

## Stories used (all facts read from sources on 22 Nov 2026; nothing invented)

1. **LEAD — Iran claims strikes on U.S. Patriot radars in Bahrain.**
   IRGC said late Saturday 21 Nov it fired missiles and drones at two
   Patriot radars at the al-Riffa and Awali bases, in retaliation for
   alleged U.S. MQ-1/MQ-9 drone incursions; Bahrain said a civilian
   industrial facility was hit instead (fire, no casualties); the U.S. has
   not confirmed damage. Sources: ANI via webindia123
   (news.webindia123.com, 22 Nov 04:11 IST), IRNA/RT via kamumedya.com,
   Al Jazeera via ANI, euronews via archynewsy.com.
2. **Russia fires ~550 drones and missiles at Ukraine overnight.**
   Zelenskyy: at least 5 killed, 10 injured; Ukraine air force counted 496
   drones and 53 missiles; a family of four died in Lapaivka, Lviv region;
   impacts in nine regions. Source: AP via KVNU (kvnutalk.com).
3. **Mexico captures "El Chapo Isidro".** Fausto Isidro Meza Flores,
   FBI Ten Most Wanted fugitive and Beltrán Leyva leader, seized in
   Guasave, Sinaloa, Friday night with U.S. intelligence help; 11 dead
   (7 suspected gunmen, 4 soldiers); flown to Mexico City. Sources: AP
   via WJSU (wjsu.org, 21 Nov) and Reflector; Reuters via LA Post.
4. **COP31 into a second day of overtime in Antalya.** Nearly 200 nations
   deadlocked on Sunday; Thursday draft stripped all mention of fossil
   fuels; EU climate chief: "a good deal or no deal"; third draft promised.
   Sources: Reuters via KTWB (21 Nov), AFP via KLSE Screener (22 Nov).
5. **EU and Indonesia sign landmark trade deal.** Signed in Brussels
   Saturday 21 Nov after nearly 10 years of talks; tariffs on up to 98.5%
   of goods to be eliminated; ~€650m/year duty savings for EU exporters.
   Sources: European Commission (commission.europa.eu, reviewed 21 Nov),
   europesays.com.
6. **ALSO TODAY strip.**
   - Hong Kong: Election Committee Subsector elections open 9am–6pm;
     856 candidates for 723 seats (China Daily Asia, 22 Nov 08:53;
     Hong Kong gov info.gov.hk).
   - Peru: magnitude 6.7 quake near Carhuamayo, 108 km deep, felt in Lima;
     no casualties or damage (USGS via AP/Reflector, 21 Nov).
   - Myanmar: magnitude 4.1 quake early Sunday (National Centre for
     Seismology via ANI/Desi Talk Chicago).
   - United States: FBI reportedly investigating an apparent hack of its
     criminal database (BBC via NewsBites, 22 Nov 00:10 UTC).

## Build

- `render.py` written fresh in this work dir (Pillow + DejaVu Serif;
  navy/cream broadsheet, 1024x1024). No file was copied from the
  news-image-20/21 work dirs and no other entrant's code was read.
- `main.py`: Python 3 standard-library-only, copies shipped `entry.png`
  to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).

## Verification

- `entry.png`: 1024x1024, RGB, 164,325 bytes (≤ 1,048,576).
- sha256: 0e6a1a3790bc05d9de2d5a07e51c95cbcd1d28242725c9c8f972904e58b03bd5
- `main.py` run twice with different `MAKEFUN_OUTPUT_DIR` values
  (/tmp/out1, /tmp/out2): both outputs byte-identical to each other and
  to `entry.png` (sha256 match + `cmp` clean).
- Image inspected visually (full frame + bottom-strip crop): masthead,
  dateline, BREAKING NEWS banner, lead story, 2x2 grid, ALSO TODAY strip
  (all 4 items) and footer are all legible, with no overlap or clipping.
  First render clipped the footer; spacing was tightened and re-verified.
