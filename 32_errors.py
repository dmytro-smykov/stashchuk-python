def image_info(image):
    if ("image_id" not in image) or ("image_title" not in image):
        raise TypeError(
            "Должны быть указаны image_id и image_title")
    return f"image {image['image_title']} has id {image ['image_id']}"


print(image_info({'image_title': 'car', 'image_id': 156}))

try:
    print(image_info({'image_id': 156}))
except TypeError as e:
    print(e)
