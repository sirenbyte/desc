### Using Filter

You can filter the dataset by criteria. It can also be used for equality based. Filter accepts a function that keeps elements that return True, and filters out the remaining elements.

```
PCollection<String> allStrings = pipeline
        .apply(Create.of(List.of("Hello","world","Hi")));
                
PCollection<String> filteredStrings = allStrings
        .apply(Filter.by(new SerializableFunction<String, Boolean>() {
            @Override
            public Boolean apply(String input) {
                return input.length() > 3;
            }
        }));
```

### Prepared methods

The Java SDK has already prepared comparison methods

```
PCollection<Long> numbers = Create.of(1L, 2L, 3L, 4L, 5L);
PCollection<Long> bigNumbers = numbers.apply(Filter.greaterThan(3L));
PCollection<Long> smallNumbers = numbers.apply(Filter.lessThanEq(3L));
PCollection<Long> equalNumbers = numbers.apply(Filter.equal(3L));
```


