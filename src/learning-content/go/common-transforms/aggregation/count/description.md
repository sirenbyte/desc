### Count

Counts the number of elements within each aggregation. The Count transform has three varieties:

```CountElms()``` counts the number of elements in the entire PCollection. The result is a collection with a single element.

```
import (
	"github.com/apache/beam/sdks/go/pkg/beam"
	"github.com/apache/beam/sdks/go/pkg/beam/transforms/stats"
)

func ApplyTransform(s beam.Scope, input beam.PCollection) beam.PCollection {
	return stats.CountElms(s, input)
}
```

```Count()``` counts how many elements are associated with each key. It ignores the values. The resulting collection has one output for every key in the input collection.

```
import (
	"github.com/apache/beam/sdks/go/pkg/beam"
	"github.com/apache/beam/sdks/go/pkg/beam/transforms/stats"
)

func ApplyTransform(s beam.Scope, input beam.PCollection) beam.PCollection {
	return stats.Count(s, input)
}
```