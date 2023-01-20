import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import io
import json
import requests
import py3Dmol
from stmol import showmol
from rdkit import Chem
from rdkit.Chem import AllChem


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

#lottie_s=load_lottiefile("suggestion.json")

selected = option_menu(
            menu_title=None,  
            options=["Home","ChemPlay","About Us"],  
            icons=["home", "joystick", "reply-all-fill"],  
            menu_icon="cast",  
            default_index=0,  
            orientation="horizontal",
        )

def side():
    with st.sidebar:
        st.image("x-mol.png")
        st.title("X-Mol - World of Chemistry")
        

if (selected=="Home"):
    side()
    
    def mol(smi):
        mol = Chem.MolFromSmiles(smi)
        mol = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol)
        molecule = Chem.MolToMolBlock(mol)
        return molecule

    def render(m):
        mview = py3Dmol.view()
        mview.addModel(m,'mol')
        mview.setStyle({'stick':{}})
        mview.setBackgroundColor('white')
        mview.zoom(1, 200)
        mview.zoomTo()
        showmol(mview,height=400,width=500)
    st.markdown("<h1 style='text-align: center; '>X-Mol - Explore Molecular Structure </h1>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        st.text("")
        st.text("")
        st.markdown("![Alt Text](https://media.tenor.com/ZZl5JnTJo9oAAAAM/polar-molecules-partial-charges.gif)")
    with col4:
        st.subheader("Are you worried about remembering the Nomenclature, SMILES and Structure of Compounds ?")
        st.write("Don't worry, Making logic clear will help you out to understand the structure in a more better way, Practicing ✍️ everyday can make you better drawing structure from SMILES")
    st.markdown("---")


    def iupac(smiles):
        rep = "iupac_name"
        url = nom.format(smiles, rep)
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    col1, col2 = st.columns(2)
    with col1:
        st.write("Please do enter SMILES (Simplified Molecular-input Line Entry System) in the below Prompt 🧪")
        st.caption("Go on and put the SMILES in the prompt to learn about the compound in a fun way with a smile 😊")
        smiles=st.text_input("", 'CCO')
    
        nom= "https://cactus.nci.nih.gov/chemical/structure/{0}/{1}"
        predict = st.button('Draw')
        st.text("")
        st.text("")
        st.write("Nomenclature:")
        st.code(iupac(smiles))

    with col2:
            struct=mol(smiles)
            
            if predict:
                render(struct)

    st.markdown("---")
    st.subheader("Time to learn smiles and get into the world of Molecules 🌎")
    st.markdown("---")
    st.subheader("Rules 📄")
    st.caption("Game can't be played, without Rules:")
    st.text('')
    st.write('''
    1. Each non-hydrogen atom is specified independently by its atomic symbol enclosed in square brackets [ ].
    
    2. Square brackets may be omitted for elements in the “organic subset” (B, C, N, O, P, S, F, Cl, Br, and I) if the proper number of implicit hydrogen atoms ⚛.
    
    3. Explicitly attached hydrogens and formal charges are always specified inside brackets【 】.
    ''')
    col7, col8 = st.columns(2)
    with col7:


        st.subheader("🔹 Symbols used to represent the bonds:")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.write(
            '''
            Single Bond   ----->  -

            Double Bond   ----->  =

            Triple Bond   ----->  #

            Aromatic Bond -----> :

            '''
        )
    with col8:
        st.subheader("🔹 Examples")
        st.code(
            '''
SMILES       Name      Molecular

CC        Ethane          (CH3CH3)

C=C       Ethene          (CH2CH2)

C#C       Ethyne           (CHCH)

COC    Dimethyl ether     (CH3OCH3)

CC=O   Acetaldehyde       (CH3-CH=O)

C#N    Hydrogen Cyanide      (HCN)
            '''
        )
    st.markdown("---")
    st.subheader("I guess 🤔, you're ready now. To make your own smiles")

    level = st.selectbox('How much ready are you ? Choose the Diffculty Level 🎚️:',('Easy 😅', 'Intermediate 😃', 'Difficult 💪', 'Extreme Difficult🤓'))
    def score(marks):
            if marks>1:
                    st.warning(f'Congratulation 🎉, You scored {marks}/3')
            else:
                    st.warning(f'Do not worry, Go practice more!!! You scored {marks}/3')
    if (level=="Easy 😅"):
        st.subheader("Write the nomenclature of given SMILES:")
        
        col5, col6 = st.columns(2)
        with col5:
            st.text("")
            st.text("")
            st.text("")
            st.write("Q1) CC")
            st.text("")
            st.text("")
            st.text("")
            st.write("Q2) CC=C")
            st.text("")
            st.text("")
            st.text("")
            st.write("Q3) CC(=O)O")
        with col6:
            marks=0
    
            a=st.text_input("Answer Q1:")
            b=st.text_input("Answer Q2:")
            c=st.text_input("Answer Q3:")
            submit=st.button("Submit")
            
            if submit:
                st.balloons()
                if (a.lower()=="ethane"):
                    marks+=1
                    if (b.lower()=="prop-1-ene"):
                        marks+=1
                        if (c.lower()=="ethanoic acid"):
                            marks+=1
                score(marks)

    if (level=="Intermediate 😃"):
        st.subheader("Write the nomenclature of given structure:")
        
        col5, col6 = st.columns(2)
        with col5:

            st.write("Q1)")
            st.image('q3.jpg')

            st.write("Q2)")
            st.image('q1.jpg')

            st.write("Q3)")
            st.image('q2.jpg')


        with col6:
            marks=0
    
            a=st.text_input("Answer Q1:")
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            b=st.text_input("Answer Q2:")
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            b=st.text_input("Answer Q3:")
            submit=st.button("Submit")
            
            if submit:
                st.balloons()
                if (a=="pent-1-ene"):
                    marks+=1
                    if (b=="4-methlyhex-1-ene"):
                        marks+=1
                        if (c=="2-methylbut-2-ene"):
                            marks+=1
                score(marks)
    if (level=="Extreme Difficult🤓"):
        st.subheader("Write the nomenclature of given structure:")
        
        col5, col6 = st.columns(2)
        with col5:

            st.write("Q1)")
            st.image('q4.jpg')


        with col6:
            marks=0
    
            a=st.text_input("Answer Q1:")
            submit=st.button("Submit")
            
            if submit:
                st.balloons()
                if (a=="1-ethenyl-2-hexenylcyclopropane"):
                    marks+=1
                score(marks)

    st.markdown("---")
    st.subheader("Resources to follow up and learn more 📖")
    st.warning("Nomenclature Part 1: (Previous Year MHT-CET)")
    st.video('https://www.youtube.com/watch?v=mrHxq0jBRsw&t=1494s')
    st.warning("Nomenclature Part 2: (Previous Year MHT-CET)")
    st.video('https://www.youtube.com/watch?v=-P9JRYGSno8&t=1125s')

 

