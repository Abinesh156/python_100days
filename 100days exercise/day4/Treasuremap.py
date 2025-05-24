# treasure map
row1=['⬜','⬜','⬜']
row2=['⬜','⬜','⬜']
row3=['⬜','⬜','⬜']
total=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("enter a postion!!!!! :")
horizontal=int(position[0])-1
vertical=int(position[1])-1
total[horizontal][vertical]="❌"
print(f"{row1}\n{row2}\n{row3}")