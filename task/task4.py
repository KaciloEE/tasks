s = "sabrrtuwacaddabra"
final_out=""
output = ""
prev=""
for cur in s:
    if cur>=prev:
        output +=cur
        if len(final_out)<len(output):
            final_out=output
    else:
        output = cur
    prev=cur
print (final_out)
