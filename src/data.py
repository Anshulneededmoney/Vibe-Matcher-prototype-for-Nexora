import pandas as pd

data = [
    {"name": "Boho Maxi Dress", "desc": "Flowy cotton maxi with earthy tones and tassel detailing, perfect for music festivals and beach sunsets.", "vibes": ["boho", "earthy", "relaxed"]},
    {"name": "Streetwear Hoodie", "desc": "Oversized black hoodie with graffiti prints for an energetic, urban edge.", "vibes": ["urban", "energetic", "street"]},
    {"name": "Minimalist Blazer", "desc": "Sleek beige blazer with clean lines and neutral palette, made for contemporary office wear.", "vibes": ["minimal", "formal", "modern"]},
    {"name": "Cozy Knit Sweater", "desc": "Soft wool sweater in pastel cream, giving warm, stay-in-and-read vibes.", "vibes": ["cozy", "soft", "casual"]},
    {"name": "Vintage Denim Jacket", "desc": "Faded blue denim jacket with metal buttons, evokes a retro, rebellious feel.", "vibes": ["vintage", "cool", "retro"]},
    {"name": "Sporty Track Pants", "desc": "Breathable and stretchable joggers ideal for gym sessions or athleisure looks.", "vibes": ["sporty", "active", "casual"]},
    {"name": "Elegant Silk Saree", "desc": "Hand-woven silk saree in deep maroon with golden embroidery for festive elegance.", "vibes": ["elegant", "traditional", "festive"]},
    {"name": "Artsy Graphic Tee", "desc": "White cotton tee with abstract art prints, playful and expressive.", "vibes": ["artsy", "fun", "creative"]},
]

df = pd.DataFrame(data)
df
df.to_csv("data/mock_fashion.csv", index=False)
