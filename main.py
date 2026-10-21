import json
import streamlit as st

from detector import detect_sensitive_information
from context_analyzer import analyze_context
from risk_classifier import classify_risk
from redactor import redact_sensitive_information
from report_generator import generate_report
from privacy_utils import mask_sensitive_value

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="PrivacyGuard AI",
    page_icon="",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .hero {
        padding: 30px;
        border-radius: 18px;
        background: linear-gradient(135deg, #101828, #344054);
        color: white;
        margin-bottom: 25px;
    }

    .hero h1 {
        color: white;
        font-size: 38px;
        margin-bottom: 8px;
    }

    .hero p {
        color: #d0d5dd;
        font-size: 17px;
    }

    .risk-high {
        background-color: #fee4e2;
        color: #b42318;
        padding: 12px;
        border-radius: 10px;
        font-weight: bold;
        text-align: center;
    }

    .risk-medium {
        background-color: #fef0c7;
        color: #93370d;
        padding: 12px;
        border-radius: 10px;
        font-weight: bold;
        text-align: center;
    }

    .risk-low {
        background-color: #d1fadf;
        color: #027a48;
        padding: 12px;
        border-radius: 10px;
        font-weight: bold;
        text-align: center;
    }

    .section-title {
        font-size: 23px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    .stButton > button {
        width: 100%;
        border-radius: 10px;
        min-height: 45px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <h1>PrivacyGuard AI</h1>
        <p>
            Context-Aware Sensitive Information Detection
            and Redaction System 
        </p>
        <p>
            Detect sensitive information. Evaluate sharing
            risks. Protect data before it is shared.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.info(
    "Prototype notice: PrivacyGuard AI uses predefined "
    "patterns and contextual rules. It cannot guarantee "
    "that all sensitive information will be detected."
)


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.markdown(
    '<div class="section-title"> PRIVACY ANALYSIS</div>',
    unsafe_allow_html=True
)

left_col, right_col = st.columns([3, 1])

with left_col:
    user_text = st.text_area(
        "Enter text to analyse:",
        height=220,
        placeholder=(
            "Example: Rahul Sharma works at Infosys. "
            "His email is rahul@example.com."
        )
    )

with right_col:
    st.markdown("### DESTINATION")

    destination = st.selectbox(
        "Where will this information be shared?",
        [
            "Internal use",
            "External sharing",
            "Public publication"
        ]
    )

    st.caption(
        "The destination determines which predefined "
        "privacy policy is applied."
    )

    scan_button = st.button(
        "🔍 Analyse Privacy Risk",
        type="primary"
    )


# --------------------------------------------------
# ANALYSIS PIPELINE
# --------------------------------------------------

if scan_button:

    if not user_text.strip():
        st.warning("Please enter some text before scanning.")

    else:
        with st.spinner("Analysing your text..."):

            # Step 1: Detect sensitive information
            findings = detect_sensitive_information(user_text)

            # Step 2: Evaluate sharing context
            context_results = analyze_context(
                user_text,
                findings,
                destination
            )

            # Step 3: Classify overall risk
            risk_result = classify_risk(context_results)

            # Step 4: Generate sanitised text
            redacted_text = redact_sensitive_information(
                user_text,
                findings
            )

            # Step 5: Generate report
            report = generate_report(
                findings,
                context_results,
                risk_result,
                redacted_text
            )

            # Save results for display and downloads
            st.session_state["privacy_report"] = report
            st.session_state["original_text"] = user_text
            st.session_state["destination"] = destination

            # Refresh the editable sanitised-output widget on every scan.
            # Streamlit keeps keyed widget values in session_state, so if the
            # user manually cleared the text area, that old empty value can
            # otherwise override the newly generated report text.
            st.session_state["sanitised_output"] = redacted_text

        st.success("Privacy analysis completed!")


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

if "privacy_report" in st.session_state:

    report = st.session_state["privacy_report"]

    st.divider()

    st.markdown(
        '<div class="section-title">📊 Risk Dashboard</div>',
        unsafe_allow_html=True
    )

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric(
            "Detected Items",
            report["total_detected"]
        )

    with metric2:
        st.metric(
            "Overall Risk",
            report["overall_risk"]
        )

    with metric3:
        st.metric(
            "Recommended Action",
            report["decision"]
        )

    # Colour-coded risk indicator
    overall_risk = report["overall_risk"]

    if overall_risk == "HIGH":
        st.markdown(
            '<div class="risk-high">'
            '🚨 HIGH RISK — Redaction or other protective '
            'action is required under the current rules.'
            '</div>',
            unsafe_allow_html=True
        )

    elif overall_risk == "MEDIUM":
        st.markdown(
            '<div class="risk-medium">'
            '⚠️ REVIEW REQUIRED — Check the applicable '
            'privacy policy before sharing.'
            '</div>',
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            '<div class="risk-low">'
            'ℹ️ LOW RISK — No issue was identified by the '
            'current rules. This is not a safety guarantee.'
            '</div>',
            unsafe_allow_html=True
        )

    st.write("**Reason:**", report["reason"])

    # --------------------------------------------------
    # DETECTION RESULTS
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">🔎 Detection Results</div>',
        unsafe_allow_html=True
    )

    findings = report["detected_items"]

    if findings:

        st.caption(
            "Detected values are masked in this table. "
            "Masking reduces exposure but does not guarantee "
            "that every sensitive value is hidden."
        )

        st.dataframe(
            [
                {
                    "Category": item["category"],
                    "Detected Value": mask_sensitive_value(
                        item["value"],
                        item["category"]
                    ),
                    "Detection Method": item.get(
                        "method",
                        "Rule-based"
                    )
                }
                for item in findings
            ],
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info(
            "No sensitive items were detected by the "
            "current detector. This does not guarantee "
            "that the text contains no sensitive data."
        )

    # --------------------------------------------------
    # CONTEXT ANALYSIS
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">CONTEXT ANALYSIS</div>',
        unsafe_allow_html=True
    )

    context_results = report["context_analysis"]

    if context_results:

        for index, item in enumerate(context_results, start=1):

            with st.expander(
                f"{index}. {item['category']} — "
                f"{item['action']}"
            ):
                st.write("**Risk:**", item["risk"])
                st.write("**Reason:**", item["reason"])

    else:
        st.info(
            "No context-policy issues were identified "
            "by the current rules."
        )

    # --------------------------------------------------
    # SANITISED OUTPUT
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">🛡️ SANITISED OUTPUT</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Review this output before sharing. Redaction "
        "depends on the information detected by the system."
    )

    st.text_area(
        "Sanitised text",
        value=report["redacted_text"],
        height=200,
        key="sanitised_output"
    )

    st.download_button(
        label="📥 Download Sanitised Text",
        data=report["redacted_text"],
        file_name="sanitised_text.txt",
        mime="text/plain"
    )

    # --------------------------------------------------
    # DOWNLOAD REPORT
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">📄 Analysis Report</div>',
        unsafe_allow_html=True
    )

    # Build a separate privacy-conscious export.
    # Keep the internal report unchanged for the application pipeline.
    export_report = {
        "total_detected": report["total_detected"],
        "overall_risk": report["overall_risk"],
        "decision": report["decision"],
        "reason": report["reason"],
        "detected_items": [
            {
                "category": item["category"],
                "value": mask_sensitive_value(
                    item["value"],
                    item["category"]
                ),
                "method": item.get("method", "Rule-based")
            }
            for item in report["detected_items"]
        ],
        "context_analysis": [
            {
                "category": item["category"],
                "value": mask_sensitive_value(
                    item["value"],
                    item["category"]
                ),
                "risk": item["risk"],
                "action": item["action"],
                "reason": item["reason"]
            }
            for item in report["context_analysis"]
        ],
        "redacted_text": report["redacted_text"]
    }

    report_json = json.dumps(
        export_report,
        indent=4,
        ensure_ascii=False
    )

    st.download_button(
        label="📥 Download JSON Report",
        data=report_json,
        file_name="privacy_analysis_report.json",
        mime="application/json"
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "PrivacyGuard AI |"
    "Rule-based privacy analysis — not a guarantee "
    "of complete detection or compliance."
)