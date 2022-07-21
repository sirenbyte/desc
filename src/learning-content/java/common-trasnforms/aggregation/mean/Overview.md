# Mean

Transforms for computing the arithmetic mean of the elements in a collection, or the mean of the values associated with each key in a collection of key-value pairs.

```Mean.globally()``` returns a transform that then returns a collection whose contents is the mean of the input collection’s elements. If there are no elements in the input collection, it returns 0.

```
PCollection<Integer> numbers = pipeline.apply(Create.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
PCollection<Double> mean = numbers.apply(Mean.globally());
```

Output

```
5.5
```


```Mean.perKey()``` returns a transform that returns a collection that contains an output element mapping each distinct key in the input collection to the mean of the values associated with that key in the input collection.

```
PCollection<KV<String, Integer>> input = pipeline.apply(
    Create.of(KV.of("🥕", 3),
              KV.of("🥕", 2),
              KV.of("🍆", 1),
              KV.of("🍅", 4),
              KV.of("🍅", 5),
              KV.of("🍅", 3)));
PCollection<KV<String, Double>> meanPerKey = input.apply(Mean.perKey());
```

Output

```
KV{🍆, 1.0}
KV{🥕, 2.5}
KV{🍅, 4.0}
```