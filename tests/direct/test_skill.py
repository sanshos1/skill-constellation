from conftest import CONTRACT
def setup(vm,deploy,ac):
 vm.warp('2035-01-01T00:00:00+00:00');vm.sender=ac[0];x=deploy(CONTRACT);x.claim('skill-7','Incident facilitation','Facilitate a documented multi-party incident review','0x'+ac[1].hex(),'0x'+ac[2].hex(),'https://rubric.example/v1',3600);return x
def mock(vm,host,level):
 vm.mock_web(r'rubric\.example',{'status':200,'body':'Levels 0 through 5; require direct facilitation evidence.'});vm.mock_web(host.replace('.','\\.'),{'status':200,'body':'Facilitated a public incident review with decisions and follow-ups.'});vm.mock_llm(r'.*SkillConstellation bounded assessment.*','{"level":'+str(level)+',"supported":true}')
def test_two_assessors_activate_at_lower_level(direct_vm,direct_deploy,direct_accounts):
 x=setup(direct_vm,direct_deploy,direct_accounts);direct_vm.sender=direct_accounts[1];mock(direct_vm,'one.example',4);x.assess('skill-7','https://one.example/artifact');direct_vm.clear_mocks();direct_vm.sender=direct_accounts[2];mock(direct_vm,'two.example',3);x.assess('skill-7','https://two.example/artifact');r=x.get_claim('skill-7');assert r['state']=='ACTIVE' and r['final_level']==3
def test_assessor_cannot_repeat(direct_vm,direct_deploy,direct_accounts):
 x=setup(direct_vm,direct_deploy,direct_accounts);direct_vm.sender=direct_accounts[1];mock(direct_vm,'one.example',4);x.assess('skill-7','https://one.example/artifact');mock(direct_vm,'two.example',4)
 with direct_vm.expect_revert('fresh pre-approved'):x.assess('skill-7','https://two.example/artifact')
def test_forged_level_rejected(direct_vm,direct_deploy,direct_accounts):
 x=setup(direct_vm,direct_deploy,direct_accounts);mock(direct_vm,'one.example',4);r=x._score(x.claims['SKILL-7'],'https://one.example/artifact');assert direct_vm.run_validator(leader_result=r);f=dict(r);f['level']=5;assert not direct_vm.run_validator(leader_result=f)
