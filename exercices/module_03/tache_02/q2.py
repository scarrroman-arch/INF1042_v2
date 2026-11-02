# Question 2 : conversion de secondes en minutes et secondes

secondes = 367

minutes = secondes // 60  # division entière : nombre de minutes complètes
reste = secondes % 60     # modulo : secondes qui restent

print(f"{secondes} secondes = {minutes} min {reste} s")
