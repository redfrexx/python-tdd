# Refactoring

###_How to keep up and improve internal quality while maintaining and enhancing a system._

## Definition

> _Changing the structure of existing code without changing the observable behaviour_

## Why?

- Enhance the life span of existing code
- Improve understandability
- Prepare for new feature
- Minimize risk of change

## Refactorings: Individual Techniques to Change an Existing Design

[Catalog of Refactorings](https://refactoring.com/catalog/)

### Atomic Refactorings

"Atomic" (small scale) refactorings are often supported by IDEs.

- Rename
- Move
- Extract
- Inline
- Encapsulate
- Introduce variable
- Introduce Parameter
- etc.

### Aggregate Refactorings

Aggregate refactorings usually require several steps (e.g. atomic refactorings) 
and a strategy to

- Replace switch expression with polymorphism
- Replace polymorphism with switch expression
- Replace loop with pipeline / stream
- etc.

## When to Refactor

- Tidy up your code continuously
- Revisit and clean up before finishing a feature
- Plan major refactorings

## The Refactoring Rhythm

_tbd_ 

## Refactoring Patterns and Strategies

_tbd_ 