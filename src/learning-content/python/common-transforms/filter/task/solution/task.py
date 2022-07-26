import apache_beam as beam

from log_elements import LogElements

with beam.Pipeline() as p:

    (p | beam.Create(range(1, 11))
     | beam.Filter(lambda num: num % 2 == 0)
     | LogElements())

