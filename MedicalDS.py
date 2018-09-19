import time
import random
import hashlib


class MedicalTests():
    def __init__(self):
        self.name = "MedicalTests"

        # Dict: Patient ID, DateofAdmittance, LabTests

    def Generate_Random(iv, lv):
        value1 = random.uniform(iv, lv)
        value1 = format(value1, '.2f')
        return value1

    def Hash_it(self, hashr):
        return hashlib.sha224(str(hashr)).hexdigest()

    LIST_DIAG_CODE=[
        'M01.X',
        'D65',
        'C92.1',
        'M05.51',
        'C91.00',
        'G55',
        'M51',
        'O04.82',
        'C33',
        'M05.442',
        'F12.15',
        'E10.43',
        'M12.162',
        'T43.3X1',
        'C54.3',
        'F06.3',
        'K91',
        'F40.01',
        'C40.11',
        'M05.752',
        'I97.81',
        'D37.02',
        'C94.6',
        'M05.49',
        'M84.51',
        'C92.51',
        'M02.38',
        'D12.7',
        'C38.2',
        'C79.72',
        'B95.62',
        'C05.1',
        'A52.0',
        'M06.31',
        'E09.62',
        'T43.3X',
        'F21',
        'C37',
        'Z13.810',
        'O24.410',
        'Z13.83',
        'F45.41',
        'M06.222',
        'D39.12',
        'M84.552',
        'O99.41',
        'O04.86',
        'B97.11',
        'B97.34',
        'D37.3',
        'O07.32',
        'D28.0',
        'J44.1',
        'D14.0',
        'Z13.85',
        'E10.630',
        'F11',
        'H47.631',
        'C92.0',
        'C41.0',
        'M90.53',
        'D13.1',
        'M02.35',
        'C71.4',
        'Z22.31',
        'C47.2',
        'F31.4',
        'K76.5',
        'O10.113',
        'E09.649',
        'D37.1',
        'N49.2',
        'I15.2',
        'I25.82',
        'M26.6',
        'C51.2',
        'C40.11',
        'E08.42',
        'E08.32',
        'M11.052',
        'H75.01',
        'I97.110',
        'B08.72',
        'M01.X5',
        'M63.831',
        'G60.1',
        'M05.75',
        'E08.64',
        'Z22.31',
        'M02.352',
        'E10.339',
        'C40.81',
        'C19',
        'B96.2',
        'O98.611',
        'C18.6',
        'I67.81',
        'C94.02',
        'N18.4',
        'O99.35',
        'D63',
        'I51.3',
        'C92.50',
        'T46.3X6',
        'C15.8',
        'I25.84',
        'M11.072',
        'H47.42',
        'M12.162',
        'M12.111',
        'E79',
        'A42.0',
        'M63',
        'M72',
        'J14',
        'M12.161',
        'O9A.1',
        'C71.8',
        'E10.339',
        'C75.1',
        'F25.0',
        'M11.071',
        'H26.223',
        'D14',
        'F52.0',
        'F01.5',
        'C91.42',
        'C21.8',
        'G47',
        'M10.38',
        'F34.0',
        'B73.1',
        'G96.1',
        'C91.5',
        'H36',
        'Z91.15',
        'M05.5',
        'D15.0',
        'C94.0',
        'I25.75',
        'C92.12',
        'Z13.22',
        'Q60.0',
        'O26.6',
        'M05.742',
        'B95.1',
        'G30',
        'M90.511',
        'H30.812',
        'J66.1',
        'E11.32',
        'N18.1',
        'C10.2',
        'D41.4',
        'C88.3',
        'C49.8',
        'E09.41',
        'Z12',
        'H47.53',
        'M05.261',
        'E75.01',
        'M05.511',
        'C02.1',
        'B40.1',
        'E09.649',
        'E11.5',
        'H34',
        'K50.014',
        'D68.3',
        'J66.1',
        'C31.3',
        'M05.561',
        'Q61.01',
        'M24.251',
        'T46.0X5',
        'F33.1',
        'M90',
        'K57.5',
        'H43',
        'F31.6',
        'O99.712',
        'E11.64',
        'I25.812',
        'O24.1',
        'F13.151',
        'I79.0',
        'T82.4',
        'D12.1',
        'A98.3',
        'F14.180',
        'M05.252',
        'M06.051',
        'M05.722',
        'H75.03',
        'C91.1',
        'H16.433',
        'Q60.4',
        'O9A.53',
        'I25.711',
        'E10.630',
        'H42',
        'N25.1',
        'H61.192',
        'O99.611',
        'H47.0',
        'M02.37',
        'O99.411',
        'D39.11',
        'E08.641',
        'M10.31',
        'D48.4',
        'M11.05',
        'I25.110',
        'M63.851',
        'E72.4',
        'C34.2',
        'H16.433',
        'O24.111',
        'Z13.0',
        'M90.6',
        'I79.0',
        'M24.22',
        'O99.43',
        'M05.132',
        'E11.331',
        'E10.331',
        'C03.0',
        'K76.7',
        'C75.3',
        'Z12.2',
        'I08.1',
        'F52.3',
        'C94.32',
        'M06.2',
        'C69.61',
        'I08.1',
        'Q24.3',
        'O10.213',
        'O98.63',
        'E09.621',
        'K57.5',
        'C91.0',
        'M90.51',
        'E08.32',
        'M49.84',
        'D48.2',
        'F63.81',
        'O9A.5',
        'S37.812',
        'O10.13',
        'O99.43',
        'C94.22',
        'A48.2',
        'C11',
        'F16.151',
        'M05.23',
        'M84',
        'K50.01',
        'F95.1',
        'I43',
        'M90.522',
        'F14.15',
        'O24.013',
        'D55.2',
        'E09.359',
        'M49.87',
        'I25.10',
        'M90.632',
        'M05.17',
        'M90.6',
        'C72.1',
        'K71.50',
        'Z12.71',
        'M02.352',
        'C94.32',
        'F12.180',
        'S35.415',
        'K08.422',
        'O10.11',
        'C18.3',
        'O24.42',
        'C62.0',
        'M05.272',
        'D44.6',
        'C18.7',
        'E10.32',
        'F45.4',
        'C74.11',
        'E08.51',
        'G32.0',
        'M06.361',
        'E09.351',
        'F18.150',
        'E09.62',
        'H26.21',
        'D13.4',
        'E08.0',
        'H81.02',
        'Z12.13',
        'Z95.810',
        'M06.37',
        'K50.813',
        'D35.5',
        'C63.2',
        'M06.25',
        'D44.5',
        'D16.2',
        'E11.3',
        'M90.86',
        'A83.6',
        'M06.041',
        'C93.01',
        'M1A.352',
        'F11',
        'M05.441',
        'M05.732',
        'M06.34',
        'M05.741',
        'F94.2',
        'C47',
        'M10.37',
        'B33.4',
        'C67.5',
        'C76.51',
        'K50.1',
        'M10.361',
        'E87.4',
        'D89.810',
        'K08.121',
        'O26.63',
        'O9A.513',
        'E30',
        'Z49',
        'F18.17',
        'J84.842',
        'F94.1',
        'G71',
        'O46.023',
        'C18.3',
        'C79.51',
        'O99.351',
        'C16.2',
        'M90.642',
        'M01.X72',
        'E30',
        'M10.322',
        'M05.25',
        'M05.59',
        'O98.6',
        'D37.0',
        'C57.21',
        'T46.3X6',
        'D31.41',
        'K00',
        'M24.242',
        'C79.02',
        'E71.31',
        'M24.272',
        'E08.5',
        'M63.832',
        'T43.3X5',
        'D12.9',
        'D31.41',
        'M01.X1',
        'Z22.31',
        'C72.3',
        'M05.13',
        'H15',
        'M05.27',
        'N16',
        'D35.2',
        'F06.1',

    ]

    List_DIAG_VAL=[
        'Direct infection of joint in infectious and parasitic diseases classified elsewhere',
        'Disseminated intravascular coagulation [defibrination syndrome]',
        'Chronic myeloid leukemia, BCR/ABL-positive',
        'Rheumatoid polyneuropathy with rheumatoid arthritis of shoulder',
        'Acute lymphoblastic leukemia not having achieved remission',
        'Nerve root and plexus compressions in diseases classified elsewhere',
        'Thoracic, thoracolumbar, and lumbosacral intervertebral disc disorders',
        'Renal failure following (induced) termination of pregnancy',
        'Malignant neoplasm of trachea',
        'Rheumatoid myopathy with rheumatoid arthritis of left hand',
        'Cannabis abuse with psychotic disorder',
        'Type 1 diabetes mellitus with diabetic autonomic (poly)neuropathy',
        'Kaschin-Beck disease, left knee',
        'Poisoning by phenothiazine antipsychotics and neuroleptics, accidental (unintentional)',
        'Malignant neoplasm of fundus uteri',
        'Mood disorder due to known physiological condition',
        'Intraoperative and postprocedural complications and disorders of digestive system, not elsewhere classified',
        'Agoraphobia with panic disorder',
        'Malignant neoplasm of short bones of right upper limb',
        'Rheumatoid arthritis with rheumatoid factor of left hip without organ or systems involvement',
        'Intraoperative cerebrovascular infarction',
        'Neoplasm of uncertain behavior of tongue',
        'Myelodysplastic disease, not classified',
        'Rheumatoid myopathy with rheumatoid arthritis of multiple sites',
        'Pathological fracture in neoplastic disease, shoulder',
        'Acute myelomonocytic leukemia, in remission',
        'Reiters disease, vertebrae',
        'Benign neoplasm of rectosigmoid junction',
        'Malignant neoplasm of posterior mediastinum',
        'Secondary malignant neoplasm of left adrenal gland',
        'Methicillin resistant Staphylococcus aureus infection as the cause of diseases classified elsewhere',
        'Malignant neoplasm of soft palate',
        'Cardiovascular and cerebrovascular syphilis',
        'Rheumatoid nodule, shoulder',
        'Drug or chemical induced diabetes mellitus with skin complications',
        'Poisoning by, adverse effect of and underdosing of phenothiazine antipsychotics and neuroleptics',
        'Schizotypal disorder',
        'Malignant neoplasm of thymus',
        'Encounter for screening for upper gastrointestinal disorder',
        'Gestational diabetes mellitus in pregnancy, diet controlled',
        'Encounter for screening for respiratory disorder NEC',
        'Pain disorder exclusively related to psychological factors',
        'Rheumatoid bursitis, left elbow',
        'Neoplasm of uncertain behavior of left ovary',
        'Pathological fracture in neoplastic disease, left femur',
        'Diseases of the circulatory system complicating pregnancy',
        'Cardiac arrest following (induced) termination of pregnancy',
        'Coxsackievirus as the cause of diseases classified elsewhere',
        'Human T-cell lymphotrophic virus, type II [HTLV-II] as the cause of diseases classified elsewhere',
        'Neoplasm of uncertain behavior of appendix',
        'Renal failure following failed attempted termination of pregnancy',
        'Benign neoplasm of vulva',
        'Chronic obstructive pulmonary disease with (acute) exacerbation',
        'Benign neoplasm of middle ear, nasal cavity and accessory sinuses',
        'Encounter for screening for nervous system disorders',
        'Type 1 diabetes mellitus with periodontal disease',
        'Opioid related disorders',
        'Disorders of visual cortex in (due to) neoplasm, right side of brain',
        'Acute myeloblastic leukemia',
        'Malignant neoplasm of bones of skull and face',
        'Osteonecrosis in diseases classified elsewhere, forearm',
        'Benign neoplasm of stomach',
        'Reiters disease, hip',
        'Malignant neoplasm of occipital lobe',
        'Carrier of bacterial disease due to meningococci',
        'Malignant neoplasm of peripheral nerves of lower limb, including hip',
        'Bipolar disorder, current episode depressed, severe, without psychotic features',
        'Hepatic veno-occlusive disease',
        'Pre-existing hypertensive heart disease complicating pregnancy, third trimester',
        'Drug or chemical induced diabetes mellitus with hypoglycemia without coma',
        'Neoplasm of uncertain behavior of stomach',
        'Inflammatory disorders of scrotum',
        'Hypertension secondary to endocrine disorders',
        'Chronic total occlusion of coronary artery',
        'Temporomandibular joint disorders',
        'Malignant neoplasm of clitoris',
        'Malignant neoplasm of short bones of right upper limb',
        'Diabetes mellitus due to underlying condition with diabetic polyneuropathy',
        'Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy',
        'Hydroxyapatite deposition disease, left hip',
        'Mastoiditis in infectious and parasitic diseases classified elsewhere, right ear',
        'Postprocedural cardiac insufficiency following cardiac surgery',
        'Yaba pox virus disease',
        'Direct infection of hip in infectious and parasitic diseases classified elsewhere',
        'Disorders of muscle in diseases classified elsewhere, right forearm',
        'Refsums disease',
        'Rheumatoid arthritis with rheumatoid factor of hip without organ or systems involvement',
        'Diabetes mellitus due to underlying condition with hypoglycemia',
        'Carrier of bacterial disease due to meningococci',
        'Reiters disease, left hip',
        'Type 1 diabetes mellitus with moderate nonproliferative diabetic retinopathy without macular edema',
        'Malignant neoplasm of overlapping sites of bone and articular cartilage of right limb',
        'Malignant neoplasm of rectosigmoid junction',
        'Escherichia coli [E. coli ] as the cause of diseases classified elsewhere',
        'Protozoal diseases complicating pregnancy, first trimester',
        'Malignant neoplasm of descending colon',
        'Acute cerebrovascular insufficiency',
        'Acute erythroid leukemia, in relapse',
        'Chronic kidney disease, stage 4 (severe)',
        'Diseases of the nervous system complicating pregnancy, childbirth, and the puerperium',
        'Anemia in chronic diseases classified elsewhere',
        'Intracardiac thrombosis, not elsewhere classified',
        'Acute myelomonocytic leukemia, not having achieved remission',
        'Underdosing of coronary vasodilators',
        'Malignant neoplasm of overlapping sites of esophagus',
        'Coronary atherosclerosis due to calcified coronary lesion',
        'Hydroxyapatite deposition disease, left ankle and foot',
        'Disorders of optic chiasm in (due to) neoplasm',
        'Kaschin-Beck disease, left knee',
        'Kaschin-Beck disease, right shoulder',
        'Disorders of purine and pyrimidine metabolism',
        'Pulmonary actinomycosis',
        'Disorders of muscle in diseases classified elsewhere',
        'Fibroblastic disorders',
        'Pneumonia due to Hemophilus influenzae',
        'Kaschin-Beck disease, right knee',
        'Malignant neoplasm complicating pregnancy, childbirth and the puerperium',
        'Malignant neoplasm of overlapping sites of brain',
        'Type 1 diabetes mellitus with moderate nonproliferative diabetic retinopathy without macular edema',
        'Malignant neoplasm of pituitary gland',
        'Schizoaffective disorder, bipolar type',
        'Hydroxyapatite deposition disease, right ankle and foot',
        'Cataract secondary to ocular disorders (degenerative) (inflammatory), bilateral',
        'Benign neoplasm of middle ear and respiratory system',
        'Hypoactive sexual desire disorder',
        'Vascular dementia',
        'Hairy cell leukemia, in relapse',
        'Malignant neoplasm of overlapping sites of rectum, anus and anal canal',
        'Sleep disorders',
        'Gout due to renal impairment, vertebrae',
        'Cyclothymic disorder',
        'Onchocerciasis without eye disease',
        'Disorders of meninges, not elsewhere classified',
        'Adult T-cell lymphoma/leukemia (HTLV-1-associated)',
        'Retinal disorders in diseases classified elsewhere',
        'Patients noncompliance with renal dialysis',
        'Rheumatoid polyneuropathy with rheumatoid arthritis',
        'Benign neoplasm of thymus',
        'Acute erythroid leukemia',
        'Atherosclerosis of native coronary artery of transplanted heart with angina pectoris',
        'Chronic myeloid leukemia, BCR/ABL-positive, in relapse',
        'Encounter for screening for metabolic disorder',
        'Renal agenesis, unilateral',
        'Liver and biliary tract disorders in pregnancy, childbirth and the puerperium',
        'Rheumatoid arthritis with rheumatoid factor of left hand without organ or systems involvement',
        'Streptococcus, group B, as the cause of diseases classified elsewhere',
        'Alzheimers disease',
        'Osteonecrosis in diseases classified elsewhere, right shoulder',
        'Haradas disease, left eye',
        'Flax-dressers disease',
        'Type 2 diabetes mellitus with mild nonproliferative diabetic retinopathy',
        'Chronic kidney disease, stage 1',
        'Malignant neoplasm of lateral wall of oropharynx',
        'Neoplasm of uncertain behavior of bladder',
        'Immunoproliferative small intestinal disease',
        'Malignant neoplasm of overlapping sites of connective and soft tissue',
        'Drug or chemical induced diabetes mellitus with neurological complications with diabetic mononeuropathy',
        'Encounter for screening for malignant neoplasms',
        'Disorders of visual pathways in (due to) vascular disorders',
        'Rheumatoid vasculitis with rheumatoid arthritis of right knee',
        'Sandhoff disease',
        'Rheumatoid polyneuropathy with rheumatoid arthritis of right shoulder',
        'Malignant neoplasm of border of tongue',
        'Chronic pulmonary blastomycosis',
        'Drug or chemical induced diabetes mellitus with hypoglycemia without coma',
        'Type 2 diabetes mellitus with circulatory complications',
        'Retinal vascular occlusions',
        'Crohns disease of small intestine with abscess',
        'Hemorrhagic disorder due to circulating anticoagulants',
        'Flax-dressers disease',
        'Malignant neoplasm of sphenoid sinus',
        'Rheumatoid polyneuropathy with rheumatoid arthritis of right knee',
        'Congenital single renal cyst',
        'Disorder of ligament, right hip',
        'Adverse effect of cardiac-stimulant glycosides and drugs of similar action',
        'Major depressive disorder, recurrent, moderate',
        'Osteopathies in diseases classified elsewhere',
        'Diverticular disease of both small and large intestine without perforation or abscess',
        'Disorders of vitreous body',
        'Bipolar disorder, current episode mixed',
        'Diseases of the skin and subcutaneous tissue complicating pregnancy, second trimester',
        'Type 2 diabetes mellitus with hypoglycemia',
        'Atherosclerosis of bypass graft of coronary artery of transplanted heart without angina pectoris',
        'Pre-existing diabetes mellitus, type 2, in pregnancy, childbirth and the puerperium',
        'Sedative, hypnotic or anxiolytic abuse with sedative, hypnotic or anxiolytic-induced psychotic disorder with hallucinations',
        'Aneurysm of aorta in diseases classified elsewhere',
        'Mechanical complication of vascular dialysis catheter',
        'Benign neoplasm of appendix',
        'Marburg virus disease',
        'Cocaine abuse with cocaine-induced anxiety disorder',
        'Rheumatoid vasculitis with rheumatoid arthritis of left hip',
        'Rheumatoid arthritis without rheumatoid factor, right hip',
        'Rheumatoid arthritis with rheumatoid factor of left elbow without organ or systems involvement',
        'Mastoiditis in infectious and parasitic diseases classified elsewhere, bilateral',
        'Chronic lymphocytic leukemia of B-cell type',
        'Localized vascularization of cornea, bilateral',
        'Renal hypoplasia, bilateral',
        'Psychological abuse complicating the puerperium',
        'Atherosclerosis of autologous vein coronary artery bypass graft(s) with angina pectoris with documented spasm',
        'Type 1 diabetes mellitus with periodontal disease',
        'Glaucoma in diseases classified elsewhere',
        'Nephrogenic diabetes insipidus',
        'Noninfective disorders of pinna, left ear',
        'Diseases of the digestive system complicating pregnancy, first trimester',
        'Disorders of optic nerve, not elsewhere classified',
        'Reiters disease, ankle and foot',
        'Diseases of the circulatory system complicating pregnancy, first trimester',
        'Neoplasm of uncertain behavior of right ovary',
        'Diabetes mellitus due to underlying condition with hypoglycemia with coma',
        'Gout due to renal impairment, shoulder',
        'Neoplasm of uncertain behavior of peritoneum',
        'Hydroxyapatite deposition disease, hip',
        'Atherosclerotic heart disease of native coronary artery with unstable angina pectoris',
        'Disorders of muscle in diseases classified elsewhere, right thigh',
        'Disorders of ornithine metabolism',
        'Malignant neoplasm of middle lobe, bronchus or lung',
        'Localized vascularization of cornea, bilateral',
        'Pre-existing diabetes mellitus, type 2, in pregnancy, first trimester',
        'Encounter for screening for diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism',
        'Osteitis deformans in neoplastic diseases',
        'Aneurysm of aorta in diseases classified elsewhere',
        'Disorder of ligament, elbow',
        'Diseases of the circulatory system complicating the puerperium',
        'Rheumatoid lung disease with rheumatoid arthritis of left wrist',
        'Type 2 diabetes mellitus with moderate nonproliferative diabetic retinopathy with macular edema',
        'Type 1 diabetes mellitus with moderate nonproliferative diabetic retinopathy with macular edema',
        'Malignant neoplasm of upper gum',
        'Hepatorenal syndrome',
        'Malignant neoplasm of pineal gland',
        'Encounter for screening for malignant neoplasm of respiratory organs',
        'Rheumatic disorders of both mitral and tricuspid valves',
        'Orgasmic disorder',
        'Mast cell leukemia, in relapse',
        'Rheumatoid bursitis',
        'Malignant neoplasm of right orbit',
        'Rheumatic disorders of both mitral and tricuspid valves',
        'Pulmonary infundibular stenosis',
        'Pre-existing hypertensive chronic kidney disease complicating pregnancy, third trimester',
        'Protozoal diseases complicating the puerperium',
        'Drug or chemical induced diabetes mellitus with foot ulcer',
        'Diverticular disease of both small and large intestine without perforation or abscess',
        'Acute lymphoblastic leukemia [ALL]',
        'Osteonecrosis in diseases classified elsewhere, shoulder',
        'Diabetes mellitus due to underlying condition with mild nonproliferative diabetic retinopathy',
        'Spondylopathy in diseases classified elsewhere, thoracic region',
        'Neoplasm of uncertain behavior of peripheral nerves and autonomic nervous system',
        'Intermittent explosive disorder',
        'Psychological abuse complicating pregnancy, childbirth and the puerperium',
        'Contusion of adrenal gland',
        'Pre-existing hypertensive heart disease complicating the puerperium',
        'Diseases of the circulatory system complicating the puerperium',
        'Acute megakaryoblastic leukemia, in relapse',
        'Nonpneumonic Legionnaires disease [Pontiac fever]',
        'Malignant neoplasm of nasopharynx',
        'Hallucinogen abuse with hallucinogen-induced psychotic disorder with hallucinations',
        'Rheumatoid vasculitis with rheumatoid arthritis of wrist',
        'Disorder of continuity of bone',
        'Crohns disease of small intestine with complications',
        'Chronic motor or vocal tic disorder',
        'Cardiomyopathy in diseases classified elsewhere',
        'Osteonecrosis in diseases classified elsewhere, left upper arm',
        'Cocaine abuse with cocaine-induced psychotic disorder',
        'Pre-existing diabetes mellitus, type 1, in pregnancy, third trimester',
        'Anemia due to disorders of glycolytic enzymes',
        'Drug or chemical induced diabetes mellitus with proliferative diabetic retinopathy without macular edema',
        'Spondylopathy in diseases classified elsewhere, lumbosacral region',
        'Atherosclerotic heart disease of native coronary artery without angina pectoris',
        'Osteitis deformans in neoplastic diseases, left forearm',
        'Rheumatoid lung disease with rheumatoid arthritis of ankle and foot',
        'Osteitis deformans in neoplastic diseases',
        'Malignant neoplasm of cauda equina',
        'Toxic liver disease with chronic active hepatitis without ascites',
        'Encounter for screening for malignant neoplasm of testis',
        'Reiters disease, left hip',
        'Mast cell leukemia, in relapse',
        'Cannabis abuse with cannabis-induced anxiety disorder',
        'Laceration of left renal vein',
        'Partial loss of teeth due to periodontal diseases, class II',
        'Pre-existing hypertensive heart disease complicating pregnancy',
        'Malignant neoplasm of hepatic flexure',
        'Gestational diabetes mellitus in childbirth',
        'Malignant neoplasm of undescended testis',
        'Rheumatoid vasculitis with rheumatoid arthritis of left ankle and foot',
        'Neoplasm of uncertain behavior of carotid body',
        'Malignant neoplasm of sigmoid colon',
        'Type 1 diabetes mellitus with mild nonproliferative diabetic retinopathy',
        'Pain disorders related to psychological factors',
        'Malignant neoplasm of medulla of right adrenal gland',
        'Diabetes mellitus due to underlying condition with diabetic peripheral angiopathy without gangrene',
        'Subacute combined degeneration of spinal cord in diseases classified elsewhere',
        'Rheumatoid nodule, right knee',
        'Drug or chemical induced diabetes mellitus with proliferative diabetic retinopathy with macular edema',
        'Inhalant abuse with inhalant-induced psychotic disorder with delusions',
        'Drug or chemical induced diabetes mellitus with skin complications',
        'Cataract with neovascularization',
        'Benign neoplasm of liver',
        'Diabetes mellitus due to underlying condition with hyperosmolarity',
        'Menieres disease, left ear',
        'Encounter for screening for malignant neoplasm of small intestine',
        'Presence of automatic (implantable) cardiac defibrillator',
        'Rheumatoid nodule, ankle and foot',
        'Crohns disease of both small and large intestine with fistula',
        'Benign neoplasm of carotid body',
        'Malignant neoplasm of scrotum',
        'Rheumatoid bursitis, hip',
        'Neoplasm of uncertain behavior of pineal gland',
        'Benign neoplasm of long bones of lower limb',
        'Type 2 diabetes mellitus with ophthalmic complications',
        'Osteopathy in diseases classified elsewhere, lower leg',
        'Rocio virus disease',
        'Rheumatoid arthritis without rheumatoid factor, right hand',
        'Acute monoblastic/monocytic leukemia, in remission',
        'Chronic gout due to renal impairment, left hip',
        'Opioid related disorders',
        'Rheumatoid myopathy with rheumatoid arthritis of right hand',
        'Rheumatoid arthritis with rheumatoid factor of left wrist without organ or systems involvement',
        'Rheumatoid nodule, hand',
        'Rheumatoid arthritis with rheumatoid factor of right hand without organ or systems involvement',
        'Disinhibited attachment disorder of childhood',
        'Malignant neoplasm of peripheral nerves and autonomic nervous system',
        'Gout due to renal impairment, ankle and foot',
        'Hantavirus (cardio)-pulmonary syndrome [HPS] [HCPS]',
        'Malignant neoplasm of bladder neck',
        'Malignant neoplasm of right lower limb',
        'Crohns disease of large intestine',
        'Gout due to renal impairment, right knee',
        'Mixed disorder of acid-base balance',
        'Acute graft-versus-host disease',
        'Complete loss of teeth due to periodontal diseases, class I',
        'Liver and biliary tract disorders in the puerperium',
        'Psychological abuse complicating pregnancy, third trimester',
        'Disorders of puberty, not elsewhere classified',
        'Encounter for care involving renal dialysis',
        'Inhalant abuse with inhalant-induced dementia',
        'Pulmonary interstitial glycogenosis',
        'Reactive attachment disorder of childhood',
        'Primary disorders of muscles',
        'Antepartum hemorrhage with disseminated intravascular coagulation, third trimester',
        'Malignant neoplasm of hepatic flexure',
        'Secondary malignant neoplasm of bone',
        'Diseases of the nervous system complicating pregnancy, first trimester',
        'Malignant neoplasm of body of stomach',
        'Osteitis deformans in neoplastic diseases, left hand',
        'Direct infection of left ankle and foot in infectious and parasitic diseases classified elsewhere',
        'Disorders of puberty, not elsewhere classified',
        'Gout due to renal impairment, left elbow',
        'Rheumatoid vasculitis with rheumatoid arthritis of hip',
        'Rheumatoid polyneuropathy with rheumatoid arthritis of multiple sites',
        'Protozoal diseases complicating pregnancy, childbirth and the puerperium',
        'Neoplasm of uncertain behavior of lip, oral cavity and pharynx',
        'Malignant neoplasm of right round ligament',
        'Underdosing of coronary vasodilators',
        'Benign neoplasm of right ciliary body',
        'Disorders of tooth development and eruption',
        'Disorder of ligament, left hand',
        'Secondary malignant neoplasm of left kidney and renal pelvis',
        'Disorders of fatty-acid oxidation',
        'Disorder of ligament, left ankle',
        'Diabetes mellitus due to underlying condition with circulatory complications',
        'Disorders of muscle in diseases classified elsewhere, left forearm',
        'Adverse effect of phenothiazine antipsychotics and neuroleptics',
        'Benign neoplasm of anus and anal canal',
        'Benign neoplasm of right ciliary body',
        'Direct infection of shoulder joint in infectious and parasitic diseases classified elsewhere',
        'Carrier of bacterial disease due to meningococci',
        'Malignant neoplasm of optic nerve',
        'Rheumatoid lung disease with rheumatoid arthritis of wrist',
        'Disorders of sclera',
        'Rheumatoid vasculitis with rheumatoid arthritis of ankle and foot',
        'Renal tubulo-interstitial disorders in diseases classified elsewhere',
        'Benign neoplasm of pituitary gland',
        'Catatonic disorder due to known physiological condition',

    ]

    EMRLABS={
        'Patient_ID':'',
        'Acetone_Quantitative_Serum': Generate_Random(0.3, 5.0),
        'Albumin_Serum': Generate_Random(3.5, 8.0),
        'Albumin_Urine': Generate_Random(50, 120),
        'Aldosterone_Serum': Generate_Random(3, 40),
        'Aldosterone_Urine': Generate_Random(3, 30),
        'Ammonia_Plasma': Generate_Random(5, 40),
        'Amylase_Serum': Generate_Random(27, 150),
        'Amylase_Urine': Generate_Random(1, 25),
        'Amylase_Creatinine_Clearance': Generate_Random(1, 8),
        'Anion_Gap': Generate_Random(75, 250),
        'Arsenic_WBlood': Generate_Random(0.2, 4.0),
        'Arsenic_Urine': Generate_Random(5, 60),
        'Ascorbic_Acid': Generate_Random(0.3, 2.5),
        'Bicarbonate_Serum': Generate_Random(20, 35),
        'BM_Myetoblast': Generate_Random(0, 3),
        'BM_Promyelocyte': Generate_Random(0, 5),
        'BM_Myetoblast_Neutrophilic': Generate_Random(5, 21),
        'BM_Myetoblast_Eosinophilic': Generate_Random(0, 3.3),
        'BM_Myetoblast_Basophilic': Generate_Random(0, 1),
        'BM_Metamyo_Neutrophilic': Generate_Random(5, 40),
        'BM_Metamyo_Eosinophilic': Generate_Random(0, 6),
        'BM_Metamyo_Basophilic': Generate_Random(0, 1),
        'BM_Segmented_Neutrophils': Generate_Random(5, 18),
        'BM_Pronormoblast': Generate_Random(0, 1.9),
        'BM_Basophilic_Normoblast': Generate_Random(0, 10),
        'BM_Polychromatic_Normoblast': Generate_Random(5, 35),
        'BM_Orthochromatic_Normoblast': Generate_Random(5, 12),
        'BM_Lymphocytes': Generate_Random(10, 21),
        'BM_Plasma_Cells': Generate_Random(0, 2),
        'BM_Monocytes': Generate_Random(0, 6),
        'CA_125_Serum': Generate_Random(0, 45),
        'CA_15_3_Serum': Generate_Random(0, 45),
        'CA_19_9_Serum': Generate_Random(0, 45),
        'Cadmium_WBlood': Generate_Random(0, 0.8),
        'Cadmium_Urine': Generate_Random(0, 15),
        'Calcitonin_Serum': Generate_Random(0, 100),
        'Calcium_Serum': Generate_Random(7, 11),
        'Calcium_Ionized_Serum': Generate_Random(4.0, 6.0),
        'Calcium_Urine': Generate_Random(50, 200),
        'Carbamazepine_Serum': Generate_Random(4, 15),
        'CabonDioxide_Serum': Generate_Random(20, 30),
        'CarbonDioxide_PCO2': Generate_Random(34, 50),
        'CarbonMonoOxide_WBlood': Generate_Random(0.5, 1.9),
        'Carotene_Serum': Generate_Random(10, 90),
        'Catecholamines_Dopamine': Generate_Random(0, 30),
        'Catecholamines_Epinephrine': Generate_Random(0, 30),
        'Catecholamines_Norepinephrine': Generate_Random(100, 1900),
        'Catecholamines_Urine_Dopamine': Generate_Random(60, 800),
        'Catecholamines_Urine_Epinephrine': Generate_Random(0, 25),
        'Catecholamines_Urine_Norepinephrine': Generate_Random(14, 100),
        'CellCount_Erythrocytes': Generate_Random(4.7, 8.0),
        'CellCount_Leukocytes ': Generate_Random(4.0, 12.0),  # 4.8 - 10.8 10^3/mcl
        'CellCount_Lymphocytes ': Generate_Random(20.0, 55.0),  # 20.5 - 51.1
        'CellCount_Monocytes ': Generate_Random(1.0, 10.0),  # 1.9 - 9.3
        'CellCount_Granulocytes ': Generate_Random(42.0, 80),  # 42.2 - 75.2
        'CellCount_Eosinophils ': Generate_Random(0, 1.0),  # 0 - 0.7
        'CellCount_Basophils ': Generate_Random(0, 0.5),  # 0 - 0.2
        'CellCount_Platelets ': Generate_Random(130, 2400),  # 130 - 400
        'Ceruloplasmin_Serum ': Generate_Random(20, 80),  # 20 - 60 mg/dl
        'Chloramphenicol_Serum ': Generate_Random(10, 30),  # 10 - 25 mcg/ml
        'Chloride_Serum ': Generate_Random(95, 120),  # 98 - 107 mmol/l
        'Chloride_Urine ': Generate_Random(110, 300),  # 110 - 250 mmol/l
        'Cholestrol_Serum ': Generate_Random(0, 220),  # <200 mg/dl
        'Cholinesterase_Serum ': Generate_Random(4.0, 15),  # 4.9 - 11.9 U/ml
        'Clonazepam_Serum ': Generate_Random(15, 70),  # 15 - 60 ng/ml
        'Copper_Serum ': Generate_Random(60, 150),  # 70-140mcg/dl
        'Copper_Urine ': Generate_Random(3, 40),  # 3-35mcg/24h
        'Mean_Corpuscular_Hemoglobin ': Generate_Random(26, 35),  # 27-31mcg/dl
        'Mean_Corpuscular_Hemoglobin_Concentration ': Generate_Random(30, 40),  # 33-37 g/dl
        'Mean_Corpuscular_Volume ': Generate_Random(75, 100),  # 80 - 94mcm
        'Cortisol_Serum ': Generate_Random(4, 25),  # 5 -23 mcg/dl
        'Cortisol_Urine ': Generate_Random(0.0, 50.0),  # <50mcg/24h
        'Creatinine_Serum ': Generate_Random(0.7, 2.0),  # 0.7 - 1.3 mg/dl
        'Creatinine_Urine ': Generate_Random(14.0, 30.0),  # 14 - 26 mg/kg
        'Creatinine_Clearance_Serum ': Generate_Random(92, 150),  # 94-140 ml/min/1.7mm
        'Cyanide_Serum ': Generate_Random(0.0, 0.005),  # 0.004 mg/l
        'Cyanide_WBlood ': Generate_Random(0.0, 0.020),  # 0.016 mg/l
        'Cyclic_AMP_Serum ': Generate_Random(4.0, 9.0),  # 4.6 - 8.6 ng/ml
        'Cyclic_AMP_Urine ': Generate_Random(0.3, 4.0),  # 0.3 - 3.6 ng/ml
        'C_Peptide_Serum ': Generate_Random(0.7, 2.0),  # 0.78 - 1.89 ng/ml
        'C_Reactive_Protien_Serum ': Generate_Random(0.0, 0.6),  # <0.5mg/dl
        'Dehydroepiandrostereone_Serum ': Generate_Random(150, 1500),  # 180- 1250 ng/dl
        'Dehydroepiandrostereone_Sulfate_Serum ': Generate_Random(50, 500),  # 59 - 452 mcg/ml
        'Desipramine_Serum ': Generate_Random(70, 300),  # 75 - 300 ng/ml
        'Diazepam_Serum ': Generate_Random(80, 1200),  # 100 - 1000 ng/ml
        'Digitoxin_Serum ': Generate_Random(15, 40),  # 20 - 35 ng/ml
        'Digioxin_Serum ': Generate_Random(0.3, 2.0),  # 0.8 - 1.5 ng/ml
        'Disopyramide_Serum ': Generate_Random(2.0, 4.0),  # 2.8 - 3.2 mcg/ml
        'Doxepin_Serum ': Generate_Random(100, 300),  # 150-250 ng/ml
        'Estradiol_Serum ': Generate_Random(8, 60),  # 10 - 50 pg/ml
        'Ethanol_WBlood ': Generate_Random(10, 1000),  # >100 mg/dl
        'Ethosuximide_Serum ': Generate_Random(30, 200),  # 40 - 100 mg/dl
        'Fat_Fecal_F ': Generate_Random(0.0, 6.0),  # 4g/d
        'Fatty_Acid_Serum ': Generate_Random(170, 350),  # 190-240 mg/dl
        'Ferritin_Serum ': Generate_Random(30, 250),  # 20 - 150 ng/ml
        'Fibrin_Degradation ': Generate_Random(0.3, 15),  # <10 mcg/ml
        'Flouride_Plasma ': Generate_Random(0.01, 0.3),  # 0.01 - 0.2 mcg/dl
        'Flouride_Urine ': Generate_Random(0.1, 3.5),  # 0.2 - 3.2 mcg/ml
        'Folate_Serum ': Generate_Random(2, 25),  # 3 - 20 ng/ml
        'Follicle_Stimulating_Harmone ': Generate_Random(0.2, 20.0),  # 1.4 - 15.4 miU/ml
        'Free_Thyroxine_Index ': Generate_Random(4.0, 7.3),  # 4.2-1.3
        'Gastrin_Serum ': Generate_Random(0.3, 200),  # <100 pg/ml
        'Gentamicin_Serum ': Generate_Random(0.3, 75),  # 5 8 mcg/ml
        'Glucose_Fasting_Blood ': Generate_Random(60, 100),  # 65-95mg/dl
        'Glocose_Fasting_Serum ': Generate_Random(60, 109),  # 74-106 mg/dl
        'Glucose_Random_Serum ': Generate_Random(0.3, 200),  # <120 mg/dl
        'Glucose_Urine ': Generate_Random(0.3, 600),  # <500 mg/24h
        'Gluthemide_Serum ': Generate_Random(2, 8),  # 2 - 6 mcg/ml
        'Glycated_Hemoglobin ': Generate_Random(4.0, 7.0),  # 4.2 - 5.9%
        'Growth_Hormone_Serum ': Generate_Random(0.3, 5.0),  # <5 ng/ml
        'Haptoglobin_Serum ': Generate_Random(30, 250),  # 30 -200 mg/dl
        'Choesterol_HDL ': Generate_Random(0.3, 50),  # >40 mg/dl
        'Cholestrol_Tryglycerides ': Generate_Random(0.3, 200),  # <150 mg/dl
        'Hematocrit ': Generate_Random(40, 60),  # 42-52%
        'Hemoglobin ': Generate_Random(10, 18),  # 14.0-18.0 g/dl
        'Hemoglobin_Plasma ': Generate_Random(0.1, 5),  # <3mg/dl
        'Hemoglobin_HbA ': Generate_Random(90,100),  # >95%
        'Hemoglobin_HbA2 ': Generate_Random(1.4, 4.0),  # 1.5-3.7%
        'Hemoglobin_HbF ': Generate_Random(0.0, 4),  # <2%
        'B_Hydroxybutyric_Acid_Serum ': Generate_Random(0.21, 3.0),  # 0.21 - 2.81 mg/dl
        'Hydroxycorticosteroids_Serum ': Generate_Random(3, 12),  # 3 -10 mg/24h
        'Immunoglobulin_IgG ': Generate_Random(700, 1700),  # 700 -1600 mg/dl
        'Immunoglobulin_IgA ': Generate_Random(70, 500),  # 70-400 mg/dl
        'Immunoglobulin_IgM ': Generate_Random(40, 250),  # 40-230 mg/dl
        'Immunoglobulin_IgD ': Generate_Random(0.0, 9.0),  # 0-8 mg/dl
        'Immunoglobulin_IgE ': Generate_Random(3, 480.0),  # 3 -423 IU/ml
        'Immunoglobulin_IgC ': Generate_Random(0.5, 8.0),  # 0.5 - 6.1 mg/dl
        'Insulin_Plasma_Fasting ': Generate_Random(2, 35.0),  # 2 -25 mcU/ml
        'Iron_Serum ': Generate_Random(65, 195.0),  # 65-175 mcg/dl
        'TICB_Serum ': Generate_Random(240, 500),  # 250-425mcg/dl
        'Iron_Saturation_Serum ': Generate_Random(20, 80),  # 20 -50%
        'Ketosteroids_Urine ': Generate_Random(8, 35),  # 10 -25 mg/24h
        'Lactate_Plasma ': Generate_Random(4.2, 25),  # 4.5 - 19.8 mg/dl
        'Lactate_WBlood ': Generate_Random(6.0, 18.0),  # 8.1 - 15.3 mg/dl
        'LDL_Cholesterol_Plasma ': Generate_Random(10, 150),  # <130 mg/dl
        'Lead_WBlood ': Generate_Random(0, 30),  # 25 mcg/dl
        'Lead_Urine ': Generate_Random(0, 60.0),  # 50 mcg/dl
        'Lidocaine_Serum ': Generate_Random(1.0, 8.0),  # 1.5 - 6.0 mcg/ml
        'Lipase_Serum ': Generate_Random(15, 300),  # 23 - 300 U/L
        'Lithium_Serum ': Generate_Random(0.3, 1.8),  # 0.6 - 1.2 mEq/l
        'Lorazepam_Serum ': Generate_Random(50, 270),  # 50-240 ng/ml
        'Luteinizing_Hormone_Serum ': Generate_Random(1.0, 9.0),  # 1.24 - 7.8 mIU/ml
        'Magnesium_Serum ': Generate_Random(1.0, 3.0),  # 1.3 - 2.1 mEq/L
        'Magnesium_Urine ': Generate_Random(6.0, 15.0),  # 6.0-10.0 mEq/24h
        'Mercury_WBlood ': Generate_Random(0.3, 70.0),  # 0.6 - 59 mcg/l
        'Mercury_Urine ': Generate_Random(0.3, 30),  # <20 mcg/d
        'Metanephrines_Urine ': Generate_Random(0.1, 2.0),  # 0.1 - 1.6 mg/24h
        'Methemoglobin ': Generate_Random(0.06, 0.5),  # 0.06 - 0.24 g/dl
        'Methotrexate_Serum ': Generate_Random(0.02, 1.0),  # 0.02 mcmol/l
        'Myelin_Basci_Protein ': Generate_Random(0.3, 3.0),  # <2.5 ng/ml
        'Myoglobin_Serum ': Generate_Random(0.0, 90),  # <85 ng/ml
        'Nortriptyline_Serum ': Generate_Random(40, 180),  # 50 - 150 ng/ml
        'Nucleotidase_Serum ': Generate_Random(2, 25),  # 2 -17 U/L
        'N_Acetylprocainamide_Serum ': Generate_Random(3, 50),  # 5 -30 mcg/ml
        'Osmolality_Serum ': Generate_Random(260, 395),  # 275 - 295 mosm
        'Osmolality_Urine ': Generate_Random(50, 1500),  # 50 -1200 mosm
        'Oxazepam_Serum ': Generate_Random(0.1, 1.9),  # 0.2 - 1.4 mcg/ml
        'Oxygen_Blood ': Generate_Random(10, 35),  # 16 - 24 vol%
        'P50_Blood ': Generate_Random(20, 50),  # 25-29 mmHg
        'Partial_Thromboplastine_Time ': Generate_Random(0.3, 45.0),  # <35 sec
        'Pentobarbital_Serum ': Generate_Random(0.3, 8.0),  # 1 - 5 mcg/ml
        'pH_Blood ': Generate_Random(6.0, 9.0),  # 7.35 - 7.45
        'pH_Urine ': Generate_Random(4.0, 9.0),  # 4.6 - 8.0
        'Phenacetin_Plasma ': Generate_Random(1, 40.0),  # 1 -30 mcg/ml
        'Phenobarbital_Serum ': Generate_Random(10, 40.0),  # 15 -40 mcg/ml
        'Phenolsulfonphthalein_Excretion_Urine ': Generate_Random(20, 59.0),  # 28 -51 %
        'Phenylalanine_Serum ': Generate_Random(0.3, 3.0),  # 0.8 - 1.8 mg/dl
        'Phenytoin_Serum ': Generate_Random(10.3, 35.0),  # 10 -20 ng/ml
        'Phosphatase_Acid_Serum ': Generate_Random(0.3, 5.0),  # <3.0 ng/ml
        'Phosphatase_Alkaline ': Generate_Random(30, 145.0),  # 38 - 126 U/L
        'Phosphate_Inorganic_Serum ': Generate_Random(2.0, 5.0),  # 2.7 - 4.5 mg/dl
        'Phospholipids_Serum ': Generate_Random(110, 305.0),  # 125 - 275 mg/dl
        'Phosphorus_Urine ': Generate_Random(0.1, 2.0),  # 0.4 - 1.3 g/24h
        'Porphyrins_Urine ': Generate_Random(30, 260.0),  # 34 - 230 mcg/24h
        'Potassium_Plasma ': Generate_Random(3.0, 6.0),  # 3.5 - 4.5 mEq/L
        'Potassium_Serum ': Generate_Random(3.0, 8.0),  # 3.5 - 5.1 mEq/L
        'Potassium_Urine ': Generate_Random(20, 150),  # 25 -125 mEq/d
        'Prealbumin_Serum ': Generate_Random(6.3, 60.0),  # 10 - 40 mg/dl
        'Prlmidone_Serum ': Generate_Random(2, 15.0),  # 5 - 12 mcg/ml
        'Progesterone_Serum ': Generate_Random(8, 100.0),  # 13 - 97 ng/dl
        'Prolactine_Serum ': Generate_Random(0.9, 25.0),  # 2.5 - 15.0 ng/ml
        'Propoxyphene_plasma ': Generate_Random(30, 155.0),  # 50 - 100 ng/ml
        'Propranolo_Serum ': Generate_Random(40.3, 155.0),  # 50 - 100 ng/ml
        'Prostate_Specific_Antigen_Serum ': Generate_Random(0.3, 5.0),  # <4.0 ng/ml
        'Protein_Serum_Albumin ': Generate_Random(0.9, 75.0),  # 3.9 - 5.1 g/dl
        'Protein_Serum_Globulin_Alpha1 ': Generate_Random(0.1, 0.8),  # 0.2 - 0.4 g/dl
        'Protein_Serum_Globulin_Alpha2 ': Generate_Random(0.3, 2.0),  # 0.4 - 0.8 g/dl
        'Protein_Serum_Globulin_Beta ': Generate_Random(0.3, 5.0),  # 0.5 - 1.0 g/dl
        'Protein_Serum_Globulin_Gema ': Generate_Random(0.3, 5.0),  # 0.6 - 1.3 g/dl
        'Protein_Urine ': Generate_Random(20, 100),  # 50 - 80 mg/24h
        'Prothrombin_Consumption ': Generate_Random(10, 50),  # >20 sec
        'Protoporphyrin_WB ': Generate_Random(10, 90),  # <60 mcg/dl
        'Pyruvate_Blood ': Generate_Random(0.3, 2.0),  # 0.3 - 0.9 mg/dl
        'Quinidine_Serum ': Generate_Random(1.2, 5.0),  # 2 - 5 mcg/dl
        'Salicylates_Serum ': Generate_Random(100, 355.0),  # 150 - 300 mcg/ml
        'Sodium_Serum ': Generate_Random(110, 175.0),  # 136 - 145 mEq/d
        'Specific_Gravity_Urine ': Generate_Random(1.0, 1.5),  # 1.002 - 1.030
        'Testosterone_Serum ': Generate_Random(240,1400),  # 280 - 1100 ng/dl
        'Theophyline_Serum ': Generate_Random(5, 50),  # 8 - 20 mcg/dl
        'Thiocyanate_Urine ': Generate_Random(0.6, 5.0),  # 1 - 4 mcg/dl
        'Thiopental_Serum ': Generate_Random(0.5, 6.0),  # 1.0 - 5.0 mcg/ml
        'Thyroid_Stimulating_Hormone ': Generate_Random(0.3, 5.0),  # 0.4 - 4.2 mcu/ml
        'Thyroxine_Serum ': Generate_Random(2.0, 15.0),  # 5 - 12 mcg/dl
        'Thyroxine_Binding_Globulin_Serum ': Generate_Random(1.0, 5.0),  # 1.2 - 3.0 mg/dl
        'Tobramycin_Serum ': Generate_Random(3, 9.0),  # 5 - 8 mcg/ml
        'Transferrin_Serum ': Generate_Random(150, 400),  # 212 - 360 mg/dl
        'Triglycerides_Serum ': Generate_Random(10, 355.0),  # <250 mg/dl
        'Triiodothyronine_Serum ': Generate_Random(60, 300),  # 100 - 200 ng/dl
        'Urea_Nitrogen_Serum ': Generate_Random(10, 24.0),  # 12:1 to 21:1
        'Uric_Acid_Serum ': Generate_Random(2.0,9.0),  # 4.5 - 8.0 mg/dl
        'Uric_Acid_Urine ': Generate_Random(200, 800),  # 250 - 750 mg/24h
        'Urobilinogen_Urine ': Generate_Random(0.3, 5.0),  # 0.5 - 4.0 Eu/d
        'Valproic_Acid_Serum ': Generate_Random(30, 150.0),  # 50 - 100 mcg/dl
        'Vancomycin_Serum ': Generate_Random(12, 50.0),  # 20 - 40 mcg/ml
        'Vanillylmandelic_acid ': Generate_Random(0.9, 8.0),  # 1.4 - 6.5 mg/24h
        'Viscosity_Serum ': Generate_Random(0.9, 2.0),  # 1.00 - 1.24 cP
        'Vitamin_A_Serum ': Generate_Random(20, 90.0),  # 30 - 80 mcg/dl
        'Vitamin_B12_Serum ': Generate_Random(90, 900.0),  # 110-800 pg/ml
        'Vitamin_E_Serum ': Generate_Random(3, 25.0),  # 5 - 18 mcg/ml
        'Zinc_Serum ': Generate_Random(50, 150.0),  # 70 - 120 mcg/dl
        'Primary_Diagnostic_Code':''
        'Primary_Diagnostic_Value'''
    }


    def Data_Loader(self, counter):
        ra=random.randint(1,272)
        self.EMRLABS['Patient_ID']=self.Hash_it(counter)
        self.EMRLABS['Primary_Diagnostic_Code']=self.LIST_DIAG_CODE[ra]
        self.EMRLABS['Primary_Diagnostic_Value']=self.List_DIAG_VAL[ra]

        return self.EMRLABS