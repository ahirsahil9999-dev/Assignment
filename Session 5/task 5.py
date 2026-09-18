# Given two scenarios — storing a user's favorite genres (which may change)
# and storing a fixed set of IRCTC train classes ('Sleeper', 'AC 3 Tier', 'AC 2 Tier') —
# choose whether to use a list or tuple for each. Write one sentence explaining your choice 
# for both.

users_favorite_genres = ["Comedy_movie","Action_movie","Horror_movie","Romance_movie"]

users_favorite_genres.pop(2)
print(users_favorite_genres)

IRCTC_train_classes = ("Sleeper","AC 3 tier","AC 2 tier")
# print(IRCTC_train_classes.pop(0)) we cannot remove item in list
print(IRCTC_train_classes)

# User's Favorite genres - List because the user may add, remove, or change their favorite genres.
# IRCTC train classes - Tuple because the set of train classes is fixed and we cannot changed.