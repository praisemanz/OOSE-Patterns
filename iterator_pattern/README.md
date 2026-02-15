# Iterator Pattern Implementation

## Pattern Description
The Iterator pattern is a behavioral design pattern that provides a way to access elements of a collection sequentially without exposing the underlying representation. It uses Python's built-in iterator protocol (`__iter__` and `__next__`).

## Use Case: Music Playlist with Multiple Iteration Strategies
This implementation models a music playlist that can be traversed in different ways: forward, reverse, shuffled, or filtered by artist.

## Class Structure

### 1. **Song** (Data Class)
- **File**: `song.py`
- **Role**: Represents a song with title, artist, and duration
- **Attributes**: `title`, `artist`, `duration`

### 2. **Playlist** (Aggregate/Collection)
- **File**: `playlist.py`
- **Role**: The collection that contains songs and creates iterators
- **Key Methods**:
  - `add_song(song)`: Add a song to the playlist
  - `__iter__()`: Returns default (forward) iterator
  - `reverse_iterator()`: Returns reverse iterator
  - `shuffle_iterator()`: Returns shuffle iterator
  - `filter_by_artist(artist)`: Returns filtered iterator

### 3. **Concrete Iterators**

#### ForwardIterator
- **File**: `forward_iterator.py`
- **Role**: Iterates from beginning to end
- **Methods**: `__iter__()`, `__next__()`

#### ReverseIterator
- **File**: `reverse_iterator.py`
- **Role**: Iterates from end to beginning
- **Methods**: `__iter__()`, `__next__()`

#### ShuffleIterator
- **File**: `shuffle_iterator.py`
- **Role**: Iterates in random order
- **Methods**: `__iter__()`, `__next__()`

#### FilterIterator
- **File**: `filter_iterator.py`
- **Role**: Iterates only over songs matching a filter condition
- **Methods**: `__iter__()`, `__next__()`

### 4. **Main Program**
- **File**: `main.py`
- **Purpose**: Demonstrates all iteration strategies

## How the Code Adheres to the Pattern

1. **Built-in Iterator Protocol**: All iterators implement Python's `__iter__()` and `__next__()` methods
2. **Separation of Concerns**: Iteration logic is separate from the collection
3. **Multiple Strategies**: Different iterators provide different traversal methods without changing the collection
4. **Independent Iterators**: Multiple iterators can traverse the same collection simultaneously
5. **Encapsulation**: Internal structure of the playlist is hidden from clients

## Class Diagram Alignment

The class diagram shows:
- **Aggregate**: `Playlist` (creates and returns iterators)
- **Iterator Interface**: Python's built-in Iterator protocol
- **Concrete Iterators**: ForwardIterator, ReverseIterator, ShuffleIterator, FilterIterator
- **Element**: `Song` (the objects being iterated)
- **Relationships**: 
  - Playlist creates iterators
  - All iterators implement the Iterator interface
  - Iterators return Song objects

## Running the Program

```bash
cd iterator_pattern
python main.py
```

## Output
The program demonstrates:
- Forward iteration (default)
- Reverse iteration
- Shuffle iteration
- Filtered iteration (by artist)
- Using iterators in list comprehensions
- Multiple simultaneous iterations

## Benefits Demonstrated
- Works seamlessly with Python's `for` loops
- Supports list comprehensions
- Multiple iteration strategies without modifying the collection
- Clean, Pythonic code

## Files in This Pattern
- `song.py` - Data class for songs
- `playlist.py` - Aggregate/Collection class
- `forward_iterator.py` - Forward iteration strategy
- `reverse_iterator.py` - Reverse iteration strategy
- `shuffle_iterator.py` - Shuffle iteration strategy
- `filter_iterator.py` - Filter iteration strategy
- `main.py` - Client code demonstrating the pattern
