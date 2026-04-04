
# ECDA: Electrical Circuit Designer & Analyzer ⚡
> **Advanced Symbolic Nodal Analysis Solver for Complex Electrical Networks**

---

## 📖 Overview
**ECDA** is a high-precision engineering tool developed to solve complex electrical circuits using **Symbolic Nodal Analysis**. Unlike standard numerical simulators that may suffer from rounding errors, ECDA leverages the power of **Symbolic Computation** to provide exact mathematical solutions for node voltages and branch currents in both **AC** and **DC** environments.

This project is tailored for engineering students and researchers who require absolute precision and deep analytical insights into circuit behavior on programming level.

---

## ✨ Key Features
* **🔍 Symbolic Solving Engine:** Powered by `SymPy` to generate exact analytical expressions and high-precision complex results.
* **🔌 Comprehensive AC/DC Support:** * **DC Analysis:** Full solution for resistive networks.
    * **AC Analysis:** Advanced handling of reactive components ($L, C$) using complex impedance and frequency-domain phasors.
* **🏗️ Automated Matrix Construction:** Dynamically builds the **Admittance Matrix ($Y$)** and **Current Vector ($I$)** for any user-defined topology.
* **⚡ Multi-Source Integration:** Supports multiple independent Voltage and Current sources within a single network.
* **🎯 Engineering Precision:** Designed to eliminate rounding errors in steady-state analysis, making it ideal for academic and industrial verification.

---

## 🛠 Tech Stack
* **Language:** Python 3.12+
* **Mathematics:** `SymPy` (Symbolic Math Library)
* **Data Structures:** `NumPy`
* **Development:** VS Code / Terminal Optimized

---

## 📊 Engineering Logic
The core of ECDA follows **Kirchhoff’s Current Law (KCL)** applied at each non-reference node to solve the matrix equation:

$$[Y][V] = [I]$$

**Where:**
* $[Y]$ is the Nodal Admittance Matrix.
* $[V]$ is the vector of unknown Node Voltages.
* $[I]$ is the vector of source currents entering the nodes.

### 💡 Example Output (Phasor Form)
```python
# Symbolic Results for an AC Circuit (60Hz)
{
    'V1': 120.00,
    'V2': 100.122 + 25.817*I, 
    'V3': 35.156 - 6.467*I,
    'I_Source': 2.961 - 1.832*I
}
```

---

## 👨‍💻 Developer
**Samer Alotaibi** *Undergraduate Electrical Engineering Student* **Umm Al-Qura University (UQU)** *Specialization: Electronics & Communications Engineering*

---

## 📜 License
This project is licensed under the **MIT License**. Created for academic excellence and engineering research.

---
