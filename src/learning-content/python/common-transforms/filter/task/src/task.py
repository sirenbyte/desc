import apache_beam as beam

from log_elements import LogElements

with beam.Pipeline() as p:

    (p | beam.Create(range(1, 11))
     # Go ahead and write here Filter with lambda
     | LogElements())

