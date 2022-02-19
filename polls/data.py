from polls.models import Voter, Vote

juan = Voter.objects.create(name='Juan')
gustavo = Voter.objects.create(name='Gustavo')
kelian = Voter.objects.create(name='Kelian')
micaela = Voter.objects.create(name='Micaela')

Vote.objects.create(voter=Voter.objects.get(name='Juan'), value='C++', year=2019)
Vote.objects.create(voter=Voter.objects.get(name='Juan'), value='Javascript', year=2020)
Vote.objects.create(voter=Voter.objects.get(name='Gustavo'), value='Javascript', year=2020)
Vote.objects.create(voter=Voter.objects.get(name='Kelian'), value='C#', year=2019)
