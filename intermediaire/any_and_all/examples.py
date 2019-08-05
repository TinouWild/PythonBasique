# Avec Any
age_invites = [5, 15, 12, 16, 20, 17]

# En France
autorisation = any(a >= 18 for a in age_invites)
print(autorisation)

# Aux USA
autorisation = any(a >= 21 for a in age_invites)
print(autorisation)

# Avec All
autorisation = all(a >= 18 for a in age_invites)
print(autorisation)

age_invites = [19, 20, 22, 41, 18, 25]
autorisation = all(a >= 18 for a in age_invites)
print(autorisation)