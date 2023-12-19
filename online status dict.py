#Without function

# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }
# count=0
# val=(statuses.values())
# l=list(val)
# for i in l:
#     if i == "online":
#         count+=1
# print(count)

#using function
def online_count(statuses):
    count=0
    val=(statuses.values())
    l=list(val)
    for i in l:
        if i == "online":
            count+=1
    return count
statuses = {"Alice": "online", "Bob": "offline","Eve": "online"}

print(online_count(statuses))
