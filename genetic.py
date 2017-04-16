import random

#
# Global variables
# Setup optimal string and GA input variables.
#

OPTIMAL     = "ACAUGCUAGAAUAGCCGCAUGUACUAGUUAA"
DNA_SIZE    = len(OPTIMAL)
POP_SIZE    = 20
GENERATIONS = 5000

#
# Helper functions
# These are used as support, but aren't direct GA-specific functions.
#

def weighted_choice(items):
  weight_total = sum((item[1] for item in items))
  n = random.uniform(0, weight_total)
  for item, weight in items:
    if n < weight:
      return item
    n = n - weight
  return item

def random_char():
  return chr(int(random.randrange(65, 90, 1)))

def random_population():
  """
  Return a list of POP_SIZE individuals, each randomly generated via iterating
  DNA_SIZE times to generate a string of random characters with random_char().
  """
  pop = []
  for i in xrange(POP_SIZE):
    dna = ""
    for c in xrange(DNA_SIZE):
      dna += random_char()
    pop.append(dna)
  return pop

#
# GA functions
# These make up the bulk of the actual GA algorithm.
#

def fitness(dna):
  """
  For each gene in the DNA, this function calculates the difference between
  it and the character in the same position in the OPTIMAL string. These values
  are summed and then returned.
  """
  fitness = 0
  for c in xrange(DNA_SIZE):
    fitness += abs(ord(dna[c]) - ord(OPTIMAL[c]))
  return fitness

def mutate(dna):
  """
  For each gene in the DNA, there is a 1/mutation_chance chance that it will be
  switched out with a random character. This ensures diversity in the
  population, and ensures that is difficult to get stuck in local minima.
  """
  dna_out = ""
  mutation_chance = 100
  for c in xrange(DNA_SIZE):
    if int(random.random()*mutation_chance) == 1:
      dna_out += random_char()
    else:
      dna_out += dna[c]
  return dna_out

def init():
    global DNAsize, geneSize, geneDiversity, geneSplit, DNA

    print("This is a very basic form of genetic software. Input variable constraints below. "
          "Good starting points are: DNA strand size (array size): 32, gene size (sub array size: 5, gene diversity (randomized 0 - x): 5"
          "gene split (where to split gene array for splicing): 2")

    DNAsize = int(input('Enter DNA strand size: '))
    geneSize = int(input('Enter gene size: '))
    geneDiversity = int(input('Enter gene diversity: '))
    geneSplit = int(input('Enter gene split: '))

    # initializes the gene population, and kicks off
    # checkDNA recursion
    initPop()
    checkDNA(DNA[0])

def crossover(dna1, dna2):
  """
  Slices both dna1 and dna2 into two parts at a random index within their
  length and merges them. Both keep their initial sublist up to the crossover
  index, but their ends are swapped.
  """
  pos = int(random.random()*DNA_SIZE)
  return (dna1[:pos]+dna2[pos:], dna2[:pos]+dna1[pos:])

#
# Main driver
# Generate a population and simulate GENERATIONS generations.
#

if __name__ == "__main__":
  # Generate initial population. This will create a list of POP_SIZE strings,
  # each initialized to a sequence of random characters.
  population = random_population()

  # Simulate all of the generations.
  for generation in xrange(GENERATIONS):
    print "Generation %s... Random sample: '%s'" % (generation, population[0])
    weighted_population = []
    for individual in population:
      fitness_val = fitness(individual)
      if generation == 4999:
        print(fitness_val);

      # Generate the (individual,fitness) pair, taking in account whether or
      # not we will accidently divide by zero.
      if fitness_val == 0:
        pair = (individual, 1.0)
      else:
        pair = (individual, 1.0/fitness_val)

      weighted_population.append(pair)

    population = []

    # Select two random individuals, based on their fitness probabilites, cross
    # their genes over at a random point, mutate them, and add them back to the
    # population for the next iteration.
    for _ in xrange(POP_SIZE/2):
      # Selection
      ind1 = weighted_choice(weighted_population)
      ind2 = weighted_choice(weighted_population)

      # Crossover
      ind1, ind2 = crossover(ind1, ind2)

      # Mutate and add back into the population.
      population.append(mutate(ind1))
      population.append(mutate(ind2))

  fittest_string = population[0]
  minimum_fitness = fitness(population[0])

  for individual in population:
    ind_fitness = fitness(individual)
    if ind_fitness <= minimum_fitness:
      fittest_string = individual
      minimum_fitness = ind_fitness

  print "Fittest String: %s" % fittest_string
  exit(0)