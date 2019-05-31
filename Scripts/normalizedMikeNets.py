#!/usr/bin/python2
# I, the author of this file, Ronald Burkey, declare it to be in the public domain.
# Use it for whatever purpose you choose.
# 
# Here's a dictionary used to translate various of Mike's signal names that can't
# be dealt with formulaically into my signal names.  Ideally this would include 
# every net, but in order to save myself effort, I'm just concentrating on those
# I know I need to reference in pooh.py, and specifically, those signals that I 
# may want to assert are HIGH at startup.  The keys are Mike's signal names, and
# the values are either AGC backplane signal names, or else NOR-gate numbers.
normalizedMikeNets = { 
	"__A02_1__cdiv_1__A":"g37103",
	"__A02_1__cdiv_1__B":"g37102",
	"__A02_1__cdiv_1__C":"g37104",
	"__A02_1__cdiv_1__D":"g37101",
	"__A02_1__cdiv_1__FS_n":"g37105", 
	"__A02_1__cdiv_1__FS":"g37106",
	"__A02_1__cdiv_2__A":"g37113",
	"__A02_1__cdiv_2__B":"g37112",
	"__A02_1__cdiv_2__C":"g37114",
	"__A02_1__cdiv_2__D":"g37111",
	"__A02_1__cdiv_2__F":"g37107",
	"__A02_1__cdiv_2__FS_n":"g37117", 
	"__A02_1__cdiv_2__FS":"g37118",
	"__A02_1__evnset":"EVNSET",
	"__A02_1__oddset":"ODDSET",
	"__A02_1__ovfstb_r4":"g37152",
	"__A02_1__ovfstb_r6":"g37154",
	"__A02_NET_133":"g37139",
	"__A02_NET_143":"g37231",
	"__A02_NET_146":"g37237",
	"__A02_NET_147":"g37238",
	"__A02_NET_149":"g37230",
	"__A02_NET_153":"g37235",
	"__A02_NET_154":"g37229",
	"__A02_NET_156":"g40246",
	"__A02_NET_158":"g37209",
	"__A02_NET_160":"g40250",
	"__A02_NET_165":"g37217",
	"__A02_NET_172":"T12SET",
	"__A02_NET_173":"T12SET",
	"__A02_NET_174":"T12SET",
	"__A02_NET_175":"T12SET",
	"__A02_NET_176":"g37347",
	"__A02_NET_183":"g37346",
	"__A02_NET_194":"g37303",
	"__A03_NET_164":"g30023",
	"__A03_NET_176":"g30037",
	"__A03_NET_177":"g30018",
	"__A03_NET_180":"g30103",
	"__A03_NET_181":"g30121",
	"__A03_NET_182":"g30109",
	"__A03_NET_185":"g49105",
	"__A03_NET_189":"g49108",
	"__A03_NET_192":"g30016",
	"__A03_NET_193":"g30018",
	"__A03_NET_194":"g30020",
	"__A03_NET_196":"g30134",
	"__A03_NET_199":"g30031",
	"__A03_NET_203":"g30032",
	"__A03_NET_205":"g30132",
	"__A03_NET_209":"g30007",
	"__A03_NET_211":"g30001",
	"__A03_NET_214":"g30115",
	"__A03_NET_216":"g30119",
	"__A03_NET_227":"g30455",
	"__A03_NET_231":"g30337",
	"__A03_NET_238":"g30331",
	"__A03_NET_239":"g30382",
	"__A03_NET_242":"g30304",
	"__A04_NET_184":"g36228", # U4020C
	"__A04_NET_187":"g36219", # U4021D
	"__A04_NET_188":"g36228", # U4024A
	"__A04_NET_193":"g36228", # U4023C U4023D
	"__A04_NET_202":"g36217", # U4017E
	"__A04_NET_209":"g36249", # U4028B
	"__A04_NET_210":"g36241", # U4030B
	"__A04_NET_214":"g36148", # U4013A
	"__A04_NET_230":"g36239", # U4025B
	"__A04_NET_232":"g36261", # U4009A
	"__A04_NET_234":"g36261", # U4006C
	"__A04_NET_235":"g36105", # U4004B
	"__A04_NET_236":"g36139", # U4003C U4003D
	"__A04_NET_237":"g36318", # U4005A
	"__A04_NET_244":"g36115", # U4006A
	"__A04_NET_254":"g36152", # U4013C
	"__A04_NET_255":"g36156", # U4016A
	"__A04_NET_257":"g36132", # U4011C
	"__A04_NET_261":"g36111", # U4001C
	"__A04_NET_262":"g36146", # U4012B
	"__A04_NET_273":"g36342", # U4043B
	"__A04_NET_274":"g36401", # U4046A
	"__A04_NET_279":"g36405", # U4045B U4045C
	"__A04_NET_281":"g36307", # U4025F
	"__A04_NET_284":"g36337", # U4038C
	"__A04_NET_286":"g36333", # U4038A
	"__A04_NET_287":"g36329", # U4035A
	"__A04_NET_307":"g36355", # U4043A
	"__A04_NET_308":"d5XP11", # U4041A
	"__A04_NET_310":"g36339", # U4040A
	"__A04_NET_311":"g36405", # U4046B
	"__A04_NET_312":"g36405", # U4046C
	"__A04_NET_313":"WG_", # U4044C
	"__A04_NET_314":"WG_", # U4043C
	"__A04_NET_316":"RB_", # U4037C
	"__A04_NET_319":"d8PP4", # U4037B
	"__A04_NET_320":"WL_", # U4062A
	"__A04_NET_321":"RC_", # U4062B
	"__A04_NET_322":"WY_", # U4059C
	"__A04_NET_323":"WY_", # U4059B
	"__A04_NET_324":"CI_", # U4060B
	"__A04_NET_325":"TSGN_", # U4060C
	"__A04_NET_326":"RB_", # U4062C
	"__A04_NET_327":"RA_", # U4057B
	"__A04_NET_328":"TMZ_", # U4060A
	"__A04_NET_329":"WG_", # U4065B
	"__A04_NET_334":"R1C_", # U4064A
	"__A04_NET_335":"RB1_", # U4060D
	"__A04_NET_336":"L16_", # U4058B
	"__A04_NET_337":"TSGN_", # U4057C
	"__A05_NET_177":"WG_", # U5011C
	"__A05_NET_178":"TSGN_", # U5011B
	"__A05_NET_179":"RG_", # U5014A
	"__A05_NET_187":"g39133", # U5011A
	"__A05_NET_189":"g", # U5014C
	"__A05_NET_193":"A2X_", # U5014B
	"__A05_NET_194":"RZ_", # U5017B
	"__A05_NET_196":"CI_", # U5017A
	"__A05_NET_203":"RB_", # U5015A
	"__A05_NET_204":"RC_", # U5013C
	"__A05_NET_208":"WA_", # U5009A
	"__A05_NET_209":"RZ_", # U5004C
	"__A05_NET_210":"RA_", # U5007C
	"__A05_NET_211":"g39105", # U5002A
	"__A05_NET_214":"MONEX_", # U5004B
	"__A05_NET_220":"RL_", # U5006B
	"__A05_NET_221":"TMZ_", # U5010B
	"__A05_NET_224":"WY_", # U5029A
	"__A05_NET_225":"g39232", # U5028D
	"__A05_NET_226":"g39230", # U5025C
	"__A05_NET_228":"g39235", # U5030C
	"__A05_NET_230":"ST2_", # U5028A
	"__A05_NET_231":"RA_", # U5027C
	"__A05_NET_234":"WA_", # U5029C
	"__A05_NET_238":"g39245", # U5032A
	"__A05_NET_239":"RC_", # U5031C
	"__A05_NET_240":"RB_", # U5016D
	"__A05_NET_244":"WZ_", # U5019C
	"__A05_NET_245":"g39209", # U5022A
	"__A05_NET_246":"WB_", # U5021B
	"__A05_NET_249":"WY12_", # U5017C
	"__A05_NET_251":"g39222", # U5026D
	"__A05_NET_253":"RU_", # U5020B
	"__A05_NET_255":"g39211", # U5023A
	"__A05_NET_256":"g39213", # U5020C
	"__A05_NET_257":"g39216", # U5025A
	"__A05_NET_258":"g39410", # U5054B
	"__A05_NET_259":"g39410", # U5055A
	"__A05_NET_260":"g39410", # U5049F U5056A
	"__A05_NET_261":"g39403", # U5022F
	"__A05_NET_266":"g39415", # U5058A
	"__A05_NET_268":"WZ_", # U5057B
	"__A05_NET_269":"Z16_", # U5057A
	"__A05_NET_271":"WA_", # U5055D
	"__A05_NET_272":"g39405", # U5054A
	"__A05_NET_276":"RC_", # U5053A
	"__A05_NET_279":"g39404", # U5046C
	"__A05_NET_282":"g39301", # U5034D U5034E
	"__A05_NET_285":"g39310", # U5039C U5039D
	"__A05_NET_286":"RU_", # U5061A
	"__A05_NET_288":"RU_", # U5061B
	"__A05_NET_289":"TOV_", # U5058D
	"__A05_NET_291":"WB_", # U5062B
	"__A05_NET_292":"WC_", # U5062C
	"__A05_NET_296":"g39348", # U5036B
	"__A05_NET_297":"g39427", # U5062A
	"__A05_NET_298":"RL_", # U5041A
	"__A05_NET_299":"g39310", # U5037C
	"__A05_NET_300":"WB_", # U5038C
	"__A05_NET_301":"WB_", # U5033A
	"__A05_NET_302":"g39310", # U5038B
	"__A05_NET_303":"RA_", # U5042A
	"__A05_NET_306":"g39318", # U5041B
	"__A05_NET_308":"g39301", # U5033B
	"__A05_NET_309":"g39301", # U5036A
	"__A05_NET_310":"WS_", # U5033C
	"__A05_NET_313":"WY12_", # U5048C
	"__A05_NET_316":"g39342", # U5022C
	"__A05_NET_317":"RB_", # U5050A
	"__A05_NET_319":"SCAD", # U5046B
	"__A05_NET_320":"SCAD", # U5048D
	"__A05_NET_323":"RZ_", # U5050B
	"__A05_NET_324":"RG_", # U5043A
	"__A05_NET_325":"g39329", # U5043B
	"__A05_NET_326":"WY_", # U5043C
	"__A05_NET_327":"RG_", # U5041C
	"__A05_NET_330":"CI_", # U5046A
	"__A05_NET_333":"A2X_", # U5045B
	"__A05_NET_334":"TMZ_", # U5057D
	"__A05_NET_335":"WL_", # U5053B
	"__A05_NET_339":"g39445", # U5063B
	"__A05_NET_341":"Z15_", # U5057C
	"__A05_NET_342":"TSGN_", # U5064A
	"__A05_NET_343":"WYD_", # U5067C
	"__A05_NET_346":"g39448", # U5063C
	"__A08_1___A1_n":"A01_", 
	"__A08_1___A2_n":"A02_",
	"__A08_2___A1_n":"A03_", 
	"__A08_2___A2_n":"A04_",
	"__A09_1___A1_n":"A05_", 
	"__A09_1___A2_n":"A06_",
	"__A09_2___A1_n":"A07_", 
	"__A09_2___A2_n":"A08_",
	"__A10_1___A1_n":"A09_", 
	"__A10_1___A2_n":"A10_",
	"__A10_2___A1_n":"A11_", 
	"__A10_2___A2_n":"A12_",
	"__A11_1___A1_n":"A13_", 
	"__A11_1___A2_n":"A14_",
	"__A08_1___Z1_n":"Z01_", 
	"__A08_1___Z2_n":"Z02_",
	"__A08_2___Z1_n":"Z03_", 
	"__A08_2___Z2_n":"Z04_",
	"__A09_1___Z1_n":"Z05_", 
	"__A09_1___Z2_n":"Z06_",
	"__A09_2___Z1_n":"Z07_", 
	"__A09_2___Z2_n":"Z08_",
	"__A10_1___Z1_n":"Z09_", 
	"__A10_1___Z2_n":"Z10_",
	"__A10_2___Z1_n":"Z11_", 
	"__A10_2___Z2_n":"Z12_",
	"__A11_1___Z1_n":"Z13_", 
	"__A11_1___Z2_n":"Z14_"
}