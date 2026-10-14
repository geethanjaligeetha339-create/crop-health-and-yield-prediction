from pathlib import Path

pdf = Path("dataset/remotesensing-11-02873.pdf")
text = ""

try:
    import fitz
    doc = fitz.open(pdf)
    text = "\n".join(page.get_text() for page in doc)
except ImportError:
    try:
        from pypdf import PdfReader
        reader = PdfReader(str(pdf))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
    except ImportError:
        print("PDF reader not installed.")
        print("Run: python -m pip install pymupdf")
        raise SystemExit(1)

terms = [
    "Sentinel-2", "band 4", "band 8", "B04", "B08",
    "NDVI", "resampled", "preprocess", "spectral band"
]

lines = text.splitlines()
matches = [
    i for i, line in enumerate(lines)
    if any(term.lower() in line.lower() for term in terms)
]

shown = set()
for i in matches:
    start, end = max(0, i - 2), min(len(lines), i + 3)
    if any(j in shown for j in range(start, end)):
        continue
    print("\n--- PDF passage ---")
    print("\n".join(lines[start:end]))
    shown.update(range(start, end))
