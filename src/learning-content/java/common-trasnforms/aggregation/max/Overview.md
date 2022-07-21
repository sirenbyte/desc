# Max

Provides a variety of different transforms for computing the maximum values in a collection, either globally or for each key.

```
PCollection<Integer> numbers = pipeline.apply(Create.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
PCollection<Double> max = input.apply(Max.doublesGlobally());
```

Output

```
10
```

Calculate the maximum of the Integers associated with each unique key (which is of type String).

```
PCollection<KV<String, Integer>> input = pipeline.apply(
    Create.of(KV.of("🥕", 3),
              KV.of("🥕", 2),
              KV.of("🍆", 1),
              KV.of("🍅", 4),
              KV.of("🍅", 5),
              KV.of("🍅", 3)));
PCollection<KV<String, Integer>> maxPerKey = input.apply(Max.integersPerKey());
```

Output

```
KV{🍅, 5}
KV{🥕, 3}
KV{🍆, 1}
```