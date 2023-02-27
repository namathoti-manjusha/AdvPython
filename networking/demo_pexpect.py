import pexpect as px
child=px.spawn("echo hcl")
result=child.expect(["welcome","to","hcl","Hello"])
print(result)