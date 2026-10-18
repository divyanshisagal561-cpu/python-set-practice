# 🐍 Python Sets Practice

A beginner-friendly Python practice project covering the **Set data structure** and its most important operations through 14 practical exercises.

This project is designed to build a strong understanding of Python Sets through simple examples and hands-on practice.

---

## 📌 About the Project

This repository contains a collection of Python exercises focused on **Sets in Python**.

The exercises progress from basic Set creation to more practical operations such as:

* Adding and removing elements
* Membership testing
* Removing duplicate values
* Union and intersection
* Difference and symmetric difference
* Subset and superset comparison
* Disjoint Sets
* Copying and clearing Sets
* Student data analysis using Sets

---

## 🎯 Learning Objectives

By completing this project, you will learn how to:

* Create and display Sets
* Add elements using `add()` and `update()`
* Remove elements using `remove()` and `discard()`
* Check the length of a Set
* Perform membership testing using `in` and `not in`
* Remove duplicate values using Sets
* Perform Set operations
* Compare Sets
* Copy and clear Sets
* Apply Set operations to a real-world student analysis example

---

## 📚 Topics Covered

| #  | Topic                  | Python Concept                     |
| -- | ---------------------- | ---------------------------------- |
| 1  | Create & Display a Set | Set creation, `type()`             |
| 2  | Add Elements           | `add()`, `update()`                |
| 3  | Remove Elements        | `remove()`, `discard()`            |
| 4  | Length & Membership    | `len()`, `in`, `not in`            |
| 5  | Remove Duplicates      | `set()`                            |
| 6  | Union                  | `union()`, `\|`                    |
| 7  | Intersection           | `intersection()`, `&`              |
| 8  | Difference             | `-`                                |
| 9  | Symmetric Difference   | `symmetric_difference()`, `^`      |
| 10 | Set Comparison         | `issubset()`, `issuperset()`, `==` |
| 11 | Disjoint Sets          | `isdisjoint()`                     |
| 12 | Copy a Set             | `copy()`                           |
| 13 | Clear a Set            | `clear()`                          |
| 14 | Student Analysis       | Combined Set operations            |

---

## 🧠 Key Concepts

### 1. Creating a Set

```python
numbers = {1, 2, 3, 4, 5}

print(numbers)
print(type(numbers))
```

### 2. Adding Elements

```python
numbers.add(40)
numbers.update([50])
```

### 3. Removing Elements

```python
numbers.remove(30)
numbers.discard(30)
```

**Difference:**

* `remove()` raises an error if the element does not exist.
* `discard()` does not raise an error if the element does not exist.

### 4. Union

Returns all unique elements from both Sets.

```python
A | B
```

or

```python
A.union(B)
```

### 5. Intersection

Returns elements common to both Sets.

```python
A & B
```

or

```python
A.intersection(B)
```

### 6. Difference

Returns elements that exist in one Set but not the other.

```python
A - B
```

### 7. Symmetric Difference

Returns elements that are present in either Set but not in both.

```python
A ^ B
```

---

## ⭐ Mini Project: Student Analysis

The final exercise applies Set operations to analyze students learning Python and SQL.

### Dataset

```python
python_students = {
    "Aman", "Riya", "Rahul", "Priya", "Neha"
}

sql_students = {
    "Riya", "Rahul", "Karan", "Neha", "Vikas"
}
```

The program finds:

1. Students learning both Python and SQL
2. Students learning only Python
3. Students learning only SQL
4. Students learning either Python or SQL but not both
5. All unique students learning Python or SQL

This combines **intersection, difference, symmetric difference, and union** in one practical example.

---

## 📁 Project Structure

```text
python-sets-practice/
│
├── set.py
├── screenshots.png
└── README.md
```

---


## 👩‍💻 Author

**Divyanshi Sagar**

BCA Student | Python Learner 
---

## ⭐ If You Find This Useful

If this project helps you understand Python Sets, feel free to ⭐ **star the repository** and explore the other projects in my GitHub profile.
