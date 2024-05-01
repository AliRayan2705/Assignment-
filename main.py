import csv
import difflib


def load_nicknames(file_path):
    nicknames = {}
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                full_name = row[0].strip().lower()
                for nickname in row[1:]:
                    nickname = nickname.strip().lower()
                    if nickname not in nicknames:
                        nicknames[nickname] = []
                    nicknames[nickname].append(full_name)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error loading nicknames from '{file_path}': {e}")
    return nicknames


def normalize_name(name):
    return name.strip().lower()


def compare_names(name1f, name1l, name2f, name2l, nicknames):
    if name1f == name2f and name1l == name2l or (name1f == name2l and name2f == name1l):
        return True

    flag1 = ((name1f in nicknames and name2f in nicknames) and (
            name2f in nicknames[name1f] or name1f in nicknames[name2f])) or name1f == name2f
    flag2 = ((name1l in nicknames and name2l in nicknames) and (
            name2l in nicknames[name1l] or name1l in nicknames[name2l])) or name2l == name1l
    if flag1 and flag2:
        return True

    # Concatenate first and last names for similarity comparison
    similarity = difflib.SequenceMatcher(None, name1f + name1l, name2f + name2l).ratio()
    return similarity >= 0.8  # Adjust this threshold based on acceptable similarity


def countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard):
    nicknames = load_nicknames('names.csv')

    names = [
        [normalize_name(billFirstName), normalize_name(billLastName)],
        [normalize_name(shipFirstName), normalize_name(shipLastName)],
        (normalize_name(billNameOnCard).split(" "))
    ]

    unique_names = set()
    for name in names:
        matched = False
        for unique_name in unique_names:
            tmp = unique_name.split(" ")
            if compare_names(name[0], name[1], tmp[0], tmp[-1], nicknames):
                matched = True
                break
        if not matched:
            unique_names.add(" ".join(name))

    return len(unique_names)
