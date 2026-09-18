# Write a generator function called insta_posts_generator(posts)  that takes a list of Instagram post captions and yields one caption at a time. Use next() to get and print the next post caption each time until all captions are printed.<br><br><em><strong>Hint:</strong> Use the yield keyword inside your function and handle StopIteration when all posts are done.</em>

def insta_posts_generator(posts):
    for post in posts:
        yield post


posts = [
    "Enjoying my day!",
    "Beautiful sunset",
    "Good vibes only!",
    "New day, new goals"
]

post_generator = insta_posts_generator(posts)

while True:
    try:
        post = next(post_generator)
        print(post)
    except StopIteration:
        break