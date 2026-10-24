def round_video_views(titles, views):
    result = [
        (title, round(view, -3))
        for title, view in zip(titles, views)
    ]
    return result


titles = ["Python Tutorial", "Gaming Video", "Cooking Tips"]
views = [125678, 2345678, 45678]

print(round_video_views(titles, views))

"""
[('Python Tutorial', 126000),
 ('Gaming Video', 2346000),
 ('Cooking Tips', 46000)]
"""