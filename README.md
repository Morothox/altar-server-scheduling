# Altar Server Scheduling Algorithm

A Python-based automatic scheduling system that fairly distributes 40 altar servers across church services over a 6-week period.

## 🚀 Features

- **Fair Distribution**: Ensures every altar server gets equal assignments
- **Sibling Pairing**: Automatically assigns siblings together
- **Availability Management**: Respects individual availability preferences
- **Absence Handling**: Loads and processes absence data from file
- **8:30 AM Requirement**: Ensures everyone serves at least once at the unpopular early service
- **Three-Phase Algorithm**: Optimizes assignments through multiple phases
- **Comprehensive Reporting**: Detailed statistics and validation reports

## 📋 Algorithm Rules

### Core Constraints
1. **Fairness**: Equal number of assignments for all servers
2. **Sibling Rule**: Siblings always assigned together
3. **No Consecutive Days**: No server works consecutive days
4. **8:30 AM Requirement**: Everyone must serve early service at least once
5. **Availability**: Only assigns servers when they're available
6. **Group Leader Distribution**: Proper distribution across services

## 🏗️ Project Structure

```
├── AltarServer.py      # Main English implementation
├── Ministrant.py       # Original German implementation
├── absences.txt        # English absence data
├── abmeldungen.txt     # German absence data
├── PROJECT_README.md   # Detailed technical documentation
└── README.md          # This file
```

## 🎯 Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd altar-server-scheduling
   ```

2. **Run the algorithm**
   ```bash
   python AltarServer.py
   ```

3. **View results**
   The program outputs:
   - Mass assignments for each service
   - Assignment statistics per server
   - Absence validation
   - 8:30 AM requirement compliance

## 📊 Sample Output

```
=== MASS OVERVIEW ===

1.04.25 at 8:30 (needs 4 servers):
  Assigned: 4 servers
    - Max (was absent)
    - Tom
    - Paul
    - Emma

=== ASSIGNMENT STATISTICS ===
Max: 2 assignments | 8:30 AM: OK
Lisa: 2 assignments | 8:30 AM: OK | Absences: 1
Tom: 3 assignments | 8:30 AM: OK
...

=== 8:30 AM REQUIREMENT CHECK ===
Everyone has at least one 8:30 service!
```

## 🗂️ Data Management

### Absence File Format (`absences.txt`)
```
# Comments start with #
Name|Date
Max|1.04.25
Lisa|8.04.25
```

### Adding New Servers
Modify the server list in `AltarServer.py`:
```python
new_server = AltarServer(
    is_group_leader=False,
    name="NewName",
    assignment_counter=0,
    siblings="SiblingName",  # Empty string if no siblings
    available=["Sunday 8:30", "Sunday 10:30"]
)
```

## 🔧 Algorithm Details

### Three-Phase System

1. **Phase 0: 8:30 AM Priority**
   - Prioritizes servers who haven't served early service
   - Ensures compliance with early service requirement

2. **Phase 1: Fair Distribution**
   - Sorts by assignment counter (least assignments first)
   - Maintains sibling pairing throughout

3. **Phase 2: Preference Optimization**
   - Attempts swaps to match server preferences
   - Improves satisfaction while preserving fairness

## 📈 Technical Specifications

- **Language**: Python 3.x
- **Servers**: 40 altar servers
- **Schedule**: 6 weeks (12 Sundays × 2 services = 24 masses)
- **Dependencies**: None (pure Python)
- **Encoding**: UTF-8 (supports international characters)

## 🌍 Multilingual Support

This project includes both German and English implementations:
- **German**: `Ministrant.py` (original)
- **English**: `AltarServer.py` (translation)

Both versions are functionally identical and can be used interchangeably.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎯 Use Cases

Perfect for:
- Churches managing altar server schedules
- Youth group coordinators
- Educational purposes (algorithm learning)
- Scheduling system examples
- Python programming practice

## 📚 Educational Value

This project demonstrates:
- Object-oriented programming in Python
- Algorithm design and optimization
- File I/O operations
- Data structure manipulation
- Constraint satisfaction problems
- Fair distribution algorithms

---

**Created with ❤️ for church communities and Python learners**