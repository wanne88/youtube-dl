from flask import Flask
from xvfbwrapper import Xvfb
import os
import openai
from pyChatGPTH import ChatGPT
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    session_token = "Token"
    api1 = ChatGPT(session_token="eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..0m4-lNdHI8pwvbXp.61GLpFycK5d8XRT9-UX1uGp3nvbqN4k0XTNtTSfu2BOeke2_g_2rZE8dhwclwubZOoGL_-_vBr7v3mkBa2JV5h5ohHQ7CgAsIkU5z3E9_HCyEU57JrkzwHpK0eqOZZo0qTCN5BeXEfv9Ujp-jg0DFfBSSteEf02IXFON55_uTjwt5_061_5alI0s5hImmZTR9Z4F9X0agyDaMX4jbVbQIfBPIDYjzkZdOPCPLtjAGwZklTyvF7ikLU95w92iRKc8JRI6ngINlaCFqErrjrgRmCvT9xu8jHqboRi3RNHxm7rQzafRtE0wB4I0YgGSm4w-BMr4lA70ROuIp_jUj9s-IzzXdZDgPrzHYFS7z-ENBJTktJ8A01c2jpJyTznxbUrrKH7HqHeUlDsmWUbk5ntx7R57N10J0mz_yCI0Uu-UcTYMz76Q0KQqs4xozSPrVou7b-mu8jNegcU3i0zu0VGUgHKx_o9y_LnV7UmeExqIT5B65x0qCrKfymKpZqeozdtKEtLpNeb_wko6h_x1XGM6U0wjnmgx56Pm2RuumUgZ-J6gakVzwdGWXQechpVykXwGpI5ECWG-LbsVzl56yyI-4ZW6F1mJYHDyNbU6uA8zbrNG1QS_ax2qhghrY0QMTDmUkR9D03L5URctrjBPKP1cJoXD9bO_Ydwk-NQwc8YhsMA08fRXPE4OAHR85AV0WEKfnymSl1e_Yb408mND0wgovQH7pm916oXIcVBnMzqBJgIWczbPHZxXSYUazRFOXymA_IMV0vmUtVpDJ62aKchKMJuAVpEaT2J79c34TYyr1nOm3GxkEnvNjnIPGsJ7_HJLA5e0IW2mchaosK1aRbtfKePFKWcN_1rC7M4k6RjmNZCr1CVsqn0wN6MA3ztM8j5wHdf6DWFz6e-aiJ_2xPBuK4tcAM0hkUTT-KOjCTRg-WtcukmXNWlQK4N_ZdBFMfS21ICx1F6GfbZs0HB5oYTJR_SNbhndTnF5GzUHLT_9sgshssrGkWx8qtQQa4ELJhsGAMeaJbzcigtVibcGOmxnYziPdBbFBV4O2gLZcWVlKkaE6CCa-9hixAKyRu9v6ZTAw73xhSNnaB2-bvFuyzXiH5pZTKRkWXP1r8uf-vQgK5psGGjNaiTrHLmssDyRzrheQjCxBNCD2jf_dL_6EuUjK0bYWiSZxz9bZoO3Zqs8acau_2LvL1ka9OjdvkdZfHgUPN2rfnTD9qNoZVD_BoINqBixnPkWmGi3BO4-7p38F6cG9pR6m8r0w9RTNEI8UUoh2Gv279NNmIt3K4Vr2d2SlbcrMo8hR_8NgSyeIf2aQcz6Krn8NlOBInX3EK3lxI6fW2vlvKrfVlCKO1CHHFZbwXeW6ymMeRCJyyGLF2iCk9LEzCL_9aKLyRC8AP3LzItPEZvJlmBUhv0SPtS_0G5H6seu0leLtbsUvrSl8Ou3Bs8O-LVw6wa_4yd2Ym-A2EyT5dkuM5TiW3tkexFfTPz6pDA5xOUqtYoR2C1Sm3TnQaFYHwQDz1__LKj8pmunAH5hYDeX5K9X3DQuntRjYz_t7er0psYkx63J_KJOUwtQkV6yInEX-eF599kZ5nRKEhJ68VtDWsMMgz_s7egLuAfdze7yLptDtoYRqZvHKGzJ0JmFmtegD9FAhxDYTLnUvEJAqXcDQNB06jIXeS8dX6gOyvBjuncQVcDRnoJe7zcwbJ9EfbBh-SMyUHq8JAUgFH_9Holvdu4E_yUjy1mtgRcPOdRhKK19eJvuwwG1wN43DowRas_38xaiBSTIGfj7pfC8cuEYCaGok7-iXYohy4iMfC_fg7IILHqm2MUAkwmNMmJzykOemo0iXFV2bYM---Ey2F3Ef5EnBeA__CWivh6CKyKvtAsYLIT7cj0M43u1SKoF5ZZ1ckjx_6v2p5QWbwGS99Mdhvh-2gxYPJpU3PxwHxANOiic_e7DRMBizECQfJMEO5uz3wG-XPLi8Cf-9vq892kHcQrUqeRCBJeP8G8mVeDMTDaLg9L6B-X_cdXa7WJNJlMkbMrJbDX-B02WXclPJlM7jj8zojoSpDF6UZhOjsx1daF7JNyU4k8szgdiwnODz_6UbUIknlQhVcwptBX0rRWNYPnBv6sL-TTKCQOxy3zeU2d_s5V_6JBx-J-Pes3IrKQukzUxpZuHNodJfbjD7WYQG9o4pmfwMgPfd654MyuBuJeJFX1fk68nRBx-r2FTPUHhjZd8qLR00aU32chj_h5-fCanfziyOoxxHRPlPKDjUE5GLOuoKEImmEIzltkJ6Ogqsyb6mMcywTm84hgzfHKFhxdakL5aWtkpfbcfIW5sKBWSj93fcY02BlctO1AwZ0StmgFSsufsp7E_eUAGH2TM38-36Ru6y2JVTC94-CVIzZh8FM_uFfGzYxaPJxM19ZWy01AyuJPz_o9FZvTJ9vghFPNAG29Vg8a4O-aXaYVp39W8O6bDhitCy5pKkEy9jzhwKYtODSQIX7GCmBSaXWyUsEhAxidrFEzHnrM2uYV1_IfOeoPuLtKo9nTt2qdfyLxBVOIw_49Wu0SltUoYO7OTm2qA_EuoECxkFRzXil6gcDqhmPj2p0UQt_9fj3QPS3nEP45sit-eRnOmFpzRduDWfgXE5LixBJAFVUbhsAn6KEaeTMttS-qXtgLyUHIOxO6VmSvGPVHVVSnSbhm90GEVBaj1oYuJ0bhtk-COGTSc1aTjMbrM-jqqtRdFIMnSmx2Mcyebfg2B_b4HqjVg4n06S4msyVVW0XUQRQ_3MDSAg-mZzw.awk7cQVH-HHarLZRs37GPg")
    while True :
        time.sleep(20)

if __name__ == '__main__':
    app.run()
