# Create a recursive function count_likes(posts) that takes a nested 
# dictionary representing Instagram posts and their replies
# (each with a 'likes' key), and returns the total number of likes 
# across all posts and replies.<br><br><em><strong>Hint:</strong> Each
# reply can itself have more replies, so use recursion to sum likes at all levels.</em>

def count_likes(posts):
    if not posts:
        return 0

    total = 0

    for post in posts:
        total += post["likes"]

        if "replies" in post:
            total += count_likes(post["replies"])

    return total


posts = [
    {
        "likes": 10,
        "replies": [
            {"likes": 5},
            {"likes": 2}
        ]
    },
    {
        "likes": 8
    }
]

result = count_likes(posts)
print("Total Likes:", result)