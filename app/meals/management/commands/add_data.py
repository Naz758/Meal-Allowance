from django.core.management.base import BaseCommand

from ...models import Department, Position, ClaimAmount


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"lists/position_list.txt") as file:
            for row in file:
                name = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                Position.objects.get_or_create(
                    name=name,
                )
        self.stdout.write(self.style.SUCCESS("list of names added"))

        with open(f"lists/department_list.txt") as file:
            for row in file:
                name = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                Department.objects.get_or_create(
                    name=name,
                )
        self.stdout.write(self.style.SUCCESS("list of names added"))
        
        with open(f"lists/claim_amount_list.txt") as file:
            for row in file:
                amount = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{amount} added"))
                ClaimAmount.objects.get_or_create(
                    amount=amount,
                )
        self.stdout.write(self.style.SUCCESS("list of amounts added"))
