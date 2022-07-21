### Using Filter

Given a predicate, filter out all elements that do not satisfy this predicate. It can also be used for filtering based on an inequality with a given value based on the order of comparison of the element.

```
PCollection<String> allStrings = pipeline
        .apply(Create.of(List.of("Hello","world")));
                
PCollection<String> filteredStrings = allStrings
        .apply(Filter.by(new SerializableFunction<String, Boolean>() {
            @Override
            public Boolean apply(String input) {
                return input.length() > 3;
            }
        }));
```

Filter accepts a function that keeps elements that return True, and filters out the remaining elements.

---

### Methods

The Java SDK has already prepared comparison methods

```
PCollection<Long> numbers = Create.of(1L, 2L, 3L, 4L, 5L);
PCollection<Long> bigNumbers = numbers.apply(Filter.greaterThan(3));
PCollection<Long> smallNumbers = numbers.apply(Filter.lessThanEq(3));
```


