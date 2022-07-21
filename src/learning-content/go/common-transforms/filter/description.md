### Using Filter
    

Given a predicate, filter out all elements that do not satisfy this predicate. It can also be used for filtering based on an inequality with a given value based on the order of comparison of the element.

```
import (
	"github.com/apache/ 
	
	fbeam/sdks/go/pkg/beam"
	"github.com/apache/beam/sdks/go/pkg/beam/transforms/filter"
)

func ApplyTransform(s beam.Scope, input beam.PCollection) beam.PCollection {
	return filter.Exclude(s, input, func(element int) bool {
		return element % 2 == 1
	})
}
```

Filter accepts a function that keeps elements that return True, and filters out the remaining elements.





