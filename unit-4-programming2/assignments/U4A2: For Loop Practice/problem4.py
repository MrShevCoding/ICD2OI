#Write a for-loop that prints both the year (starting this year)
#and your age in that year, up to the year 2100. 

# 2024 I will be 16
# In 2025 I will be 17

for i in range(2024, 2101):
    year = i 
    age = i - 2008
    print(f"{year} I will be {age}")
    
    
    # The problem here we introduced a "Magic number" 2008, what does that mean?
    # In our scenerio, it's a specific number that works in this niche secnario
    # We could have looped through age but chose to do this instead
