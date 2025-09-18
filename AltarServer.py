class AltarServer:
    def __init__(self, is_group_leader, name, assignment_counter, siblings, available):
        self.is_group_leader = is_group_leader
        self.name = name
        self.assignment_counter = assignment_counter
        self.siblings = siblings  # String with sibling names
        self.available = available  # List: ["Sunday 8:30", "Sunday 10:30"]
        self.absences = []  # List of specific absences: ["1.04.25", "8.04.25"]
        self.had_830_service = False  # Tracking for 8:30 AM requirement

class Mass:
    def __init__(self, date, time, number_of_servers, assigned):
        self.date = date  # String: "1.04.25"
        self.time = time  # String: "10:30"
        self.number_of_servers = number_of_servers  # Number: 5
        self.assigned = assigned  # List of AltarServer objects

# 40 Test altar servers (10 + 30 new)
max_server = AltarServer(True, "Max", 0, "Lisa", ["Sunday 8:30", "Sunday 10:30"])
lisa = AltarServer(False, "Lisa", 0, "Max", ["Sunday 10:30"])
tom = AltarServer(True, "Tom", 0, "", ["Sunday 8:30", "Sunday 10:30"])
anna = AltarServer(False, "Anna", 0, "Paul", ["Sunday 10:30"])
paul = AltarServer(False, "Paul", 0, "Anna", ["Sunday 8:30"])
sarah = AltarServer(True, "Sarah", 0, "", ["Sunday 10:30"])
tim = AltarServer(False, "Tim", 0, "Nina", ["Sunday 8:30", "Sunday 10:30"])
nina = AltarServer(False, "Nina", 0, "Tim", ["Sunday 10:30"])
ben = AltarServer(False, "Ben", 0, "", ["Sunday 8:30"])
lea = AltarServer(False, "Lea", 0, "", ["Sunday 10:30"])

# 30 new altar servers
felix = AltarServer(True, "Felix", 0, "Emma", ["Sunday 10:30"])
emma = AltarServer(False, "Emma", 0, "Felix", ["Sunday 8:30", "Sunday 10:30"])
jonas = AltarServer(False, "Jonas", 0, "", ["Sunday 8:30"])
maya = AltarServer(True, "Maya", 0, "Leon", ["Sunday 10:30"])
leon = AltarServer(False, "Leon", 0, "Maya", ["Sunday 8:30"])
sophie = AltarServer(False, "Sophie", 0, "", ["Sunday 10:30"])
david = AltarServer(True, "David", 0, "Mia", ["Sunday 8:30", "Sunday 10:30"])
mia = AltarServer(False, "Mia", 0, "David", ["Sunday 10:30"])
noah = AltarServer(False, "Noah", 0, "", ["Sunday 8:30"])
laura = AltarServer(False, "Laura", 0, "Finn", ["Sunday 10:30"])
finn = AltarServer(False, "Finn", 0, "Laura", ["Sunday 8:30", "Sunday 10:30"])
clara = AltarServer(True, "Clara", 0, "", ["Sunday 10:30"])
elias = AltarServer(False, "Elias", 0, "Lara", ["Sunday 8:30"])
lara = AltarServer(False, "Lara", 0, "Elias", ["Sunday 10:30"])
julian = AltarServer(False, "Julian", 0, "", ["Sunday 8:30", "Sunday 10:30"])
pia = AltarServer(True, "Pia", 0, "Theo", ["Sunday 10:30"])
theo = AltarServer(False, "Theo", 0, "Pia", ["Sunday 8:30"])
marie = AltarServer(False, "Marie", 0, "", ["Sunday 10:30"])
luis = AltarServer(False, "Luis", 0, "Nele", ["Sunday 8:30"])
nele = AltarServer(False, "Nele", 0, "Luis", ["Sunday 10:30"])
simon = AltarServer(True, "Simon", 0, "", ["Sunday 8:30", "Sunday 10:30"])
jana = AltarServer(False, "Jana", 0, "Erik", ["Sunday 10:30"])
erik = AltarServer(False, "Erik", 0, "Jana", ["Sunday 8:30"])
lena = AltarServer(False, "Lena", 0, "", ["Sunday 10:30"])
robin = AltarServer(False, "Robin", 0, "Ava", ["Sunday 8:30"])
ava = AltarServer(False, "Ava", 0, "Robin", ["Sunday 10:30"])
oliver = AltarServer(True, "Oliver", 0, "", ["Sunday 8:30", "Sunday 10:30"])
zoe = AltarServer(False, "Zoe", 0, "Kai", ["Sunday 10:30"])
kai = AltarServer(False, "Kai", 0, "Zoe", ["Sunday 8:30"])
stella = AltarServer(False, "Stella", 0, "", ["Sunday 10:30"])

# List of all altar servers (40 total)
all_servers = [max_server, lisa, tom, anna, paul, sarah, tim, nina, ben, lea,
               felix, emma, jonas, maya, leon, sophie, david, mia, noah, laura,
               finn, clara, elias, lara, julian, pia, theo, marie, luis, nele,
               simon, jana, erik, lena, robin, ava, oliver, zoe, kai, stella]

# 6-week plan: 24 masses (12 Sundays x 2 times)
# Week 1
mass1 = Mass("1.04.25", "8:30", 4, [])
mass2 = Mass("1.04.25", "10:30", 6, [])
# Week 2
mass3 = Mass("8.04.25", "8:30", 3, [])
mass4 = Mass("8.04.25", "10:30", 5, [])
# Week 3
mass5 = Mass("15.04.25", "8:30", 4, [])
mass6 = Mass("15.04.25", "10:30", 6, [])
# Week 4
mass7 = Mass("22.04.25", "8:30", 3, [])
mass8 = Mass("22.04.25", "10:30", 5, [])
# Week 5
mass9 = Mass("29.04.25", "8:30", 4, [])
mass10 = Mass("29.04.25", "10:30", 6, [])
# Week 6
mass11 = Mass("6.05.25", "8:30", 3, [])
mass12 = Mass("6.05.25", "10:30", 5, [])

# List of all masses (12 total = 6 weeks)
all_masses = [mass1, mass2, mass3, mass4, mass5, mass6,
              mass7, mass8, mass9, mass10, mass11, mass12]

# Test: Fill one mass


def find_sibling(sibling_name):
    for server in all_servers:
        if server.name == sibling_name:
            return server

    return False
            # What do you do when you find them?




def is_already_assigned(server, date, all_masses):
    for mass in all_masses:
        if mass.date == date:  # ← Only same day!
            if server in mass.assigned:
                return True
    return False

def is_absent(server, date):
    """Checks if altar server is absent for this date"""
    return date in server.absences

def needs_830_service(server):
    """Checks if altar server still needs an 8:30 service"""
    return not server.had_830_service

def mark_830_service(server):
    """Marks that altar server had an 8:30 service"""
    server.had_830_service = True

def load_absences():
    """Loads absences from text file and sets them for the altar servers"""
    try:
        with open("absences.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    parts = line.split("|")
                    if len(parts) == 2:
                        name, date = parts
                        # Find altar server and add absence
                        for server in all_servers:
                            if server.name == name:
                                server.absences.append(date)
                                break
    except FileNotFoundError:
        print("No absences.txt found - no absences loaded")




def assign_automatically():
    # PHASE 0: 8:30 AM requirement - Everyone must serve at least once at 8:30
    masses_830 = [m for m in all_masses if m.time == "8:30"]
    for mass in masses_830:
        # Sort by: needs 8:30 service, then by assignment counter
        sorted_servers = sorted(all_servers, key=lambda server: (not needs_830_service(server), server.assignment_counter))

        for server in sorted_servers:
            if (not is_already_assigned(server, mass.date, all_masses)
                and not is_absent(server, mass.date)
                and len(mass.assigned) < mass.number_of_servers):

                mass.assigned.append(server)
                server.assignment_counter += 1
                if mass.time == "8:30":
                    mark_830_service(server)

                # Assign siblings together if possible
                sibling_object = find_sibling(server.siblings)
                if (sibling_object and len(mass.assigned) < mass.number_of_servers
                    and not is_already_assigned(sibling_object, mass.date, all_masses)
                    and not is_absent(sibling_object, mass.date)):
                    mass.assigned.append(sibling_object)
                    sibling_object.assignment_counter += 1
                    if mass.time == "8:30":
                        mark_830_service(sibling_object)

    # PHASE 1: Fair distribution for all other positions
    for mass in all_masses:
        mass_string = "Sunday " + mass.time
        sorted_servers = sorted(all_servers, key=lambda server: server.assignment_counter)

        for server in sorted_servers:
            if (not is_already_assigned(server, mass.date, all_masses)
                and not is_absent(server, mass.date)
                and len(mass.assigned) < mass.number_of_servers):

                mass.assigned.append(server)
                server.assignment_counter += 1
                if mass.time == "8:30":
                    mark_830_service(server)

                # Assign siblings together
                sibling_object = find_sibling(server.siblings)
                if (sibling_object and len(mass.assigned) < mass.number_of_servers
                    and not is_already_assigned(sibling_object, mass.date, all_masses)
                    and not is_absent(sibling_object, mass.date)):
                    mass.assigned.append(sibling_object)
                    sibling_object.assignment_counter += 1
                    if mass.time == "8:30":
                        mark_830_service(sibling_object)

                if len(mass.assigned) >= mass.number_of_servers:
                    break

    # PHASE 2: Preference optimization through swapping
    for server in all_servers:
        for preferred_time in server.available:
            # Find mass that matches the preference
            for mass in all_masses:
                mass_string = "Sunday " + mass.time
                if mass_string == preferred_time:
                    # Is he already assigned? Then continue
                    if server in mass.assigned:
                        continue

                    # Find someone who wants to swap (not their preference)
                    for swap_partner in mass.assigned:
                        partner_mass_string = "Sunday " + mass.time
                        if partner_mass_string not in swap_partner.available:
                            # Partner doesn't want to be there - find where they can go
                            for other_mass in all_masses:
                                if server in other_mass.assigned:
                                    # Perform swap
                                    mass.assigned.remove(swap_partner)
                                    other_mass.assigned.remove(server)
                                    mass.assigned.append(server)
                                    other_mass.assigned.append(swap_partner)
                                    break
                            break






# assign_automatically()  # First run your algorithm

# # Then look at the results:
# print("=== RESULTS ===")
# for mass in all_masses:
#     print(f"\n{mass.date} at {mass.time} (needs {mass.number_of_servers} servers):")
#     print(f"  Assigned: {len(mass.assigned)} servers")
#     for server in mass.assigned:
#         print(f"    - {server.name}")




# Load absences before the algorithm starts
load_absences()

assign_automatically()

print("=== RESULTS WITH THREE-PHASE SYSTEM ===")
print("\n=== MASS OVERVIEW ===")
for mass in all_masses:
    print(f"\n{mass.date} at {mass.time} (needs {mass.number_of_servers} servers):")
    print(f"  Assigned: {len(mass.assigned)} servers")
    for server in mass.assigned:
        absent_text = " (was absent)" if is_absent(server, mass.date) else ""
        print(f"    - {server.name}{absent_text}")

print("\n=== ASSIGNMENT STATISTICS ===")
for server in all_servers:
    had_830 = "OK" if server.had_830_service else "NO"
    absences_text = f" | Absences: {len(server.absences)}" if server.absences else ""
    print(f"{server.name}: {server.assignment_counter} assignments | 8:30 AM: {had_830}{absences_text}")

print("\n=== ABSENCE CHECK ===")
for server in all_servers:
    if server.absences:
        print(f"{server.name}: {server.absences}")

print("\n=== 8:30 AM REQUIREMENT CHECK ===")
without_830 = [server.name for server in all_servers if not server.had_830_service]
if without_830:
    print(f"Still no 8:30 service: {', '.join(without_830)}")
else:
    print("Everyone has at least one 8:30 service!")