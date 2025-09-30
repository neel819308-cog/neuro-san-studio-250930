# Banking Operations with TRUST Evaluation Layer

## Overview
Created `banking_ops_trust.hocon` - a comprehensive agent network combining operational banking services with a responsible AI evaluation framework.

## File Location
- **Configuration**: `registries/banking_ops_trust.hocon`
- **Status**: Active (added to `manifest.hocon`)

## Architecture

### Operational Layer
**Front Man**: `customer_service_representative`
- Primary interface for all customer interactions
- Delegates to specialised banking agents
- Has access to TRUST BRAIN for responsible AI oversight

**Banking Agents**:
- `account_manager` → relationship_manager, wealth_management_advisor, investment_specialist
- `fraud_prevention_specialist` → fraud_investigation_team, security_analyst
- `loan_officer` → underwriter, mortgage_specialist, business_banking_officer
- Supporting specialists: portfolio_manager, trading_desk

### TRUST Evaluation Layer

**TRUST BRAIN** (Top-level orchestrator)
- Coordinates entire responsible AI validation process
- Provides consolidated evaluation reports
- Accessible from customer_service_representative

**TRUST Regulator** (Compliance coordinator)
- Ensures adherence to ethical and regulatory standards
- Coordinates the 5 pillars of responsible AI

**Five Pillars**:

1. **Pillar 1: S,S&R** (Safety, Security & Robustness)
   - Threat modelling, vulnerability assessment
   - Financial advice accuracy validation
   - Customer data protection checks
   - Regulatory compliance (FCA, PCI DSS, GDPR)

2. **Pillar 2: T&E** (Transparency & Explainability)
   - AI disclosure verification
   - Decision explainability assessment
   - Consumer credit regulation compliance
   - Model card and documentation review

3. **Pillar 3: Fair** (Fairness)
   - Bias detection in lending decisions
   - Equal treatment verification
   - Protected characteristics monitoring
   - Fair lending laws compliance

4. **Pillar 4: A&G** (Accountability & Governance)
   - Policy compliance verification
   - Audit trail assessment
   - Model risk management
   - Third-party risk oversight

5. **Pillar 5: C&R** (Contestability & Redress)
   - Customer challenge mechanisms
   - Complaint handling evaluation
   - Financial Ombudsman compatibility
   - Redress procedure assessment

## Usage Examples

### Standard Banking Query
```
User: "I'd like to apply for a mortgage"
→ customer_service_representative delegates to loan_officer → mortgage_specialist
```

### Responsible AI Evaluation
```
User: "Please evaluate the responsible AI compliance of how we handled the last customer interaction"
→ customer_service_representative → TRUST BRAIN → TRUST Regulator → 5 Pillars
```

### Regulatory Inquiry
```
User: "Show me how you ensure fairness in loan decisions"
→ customer_service_representative → TRUST BRAIN → TRUST Regulator → Pillar 3: Fair
```

### Specific Pillar Query
```
User: "Evaluate the transparency and explainability of our AI decision-making"
→ TRUST BRAIN → TRUST Regulator → Pillar 2: T&E
```

## Demo Mode Features

### `demo_mode`
- Applied to operational banking agents
- Generates realistic banking responses
- Simulates access to customer data and systems

### `trust_demo_mode`
- Applied to TRUST evaluation agents
- Provides realistic responsible AI assessments
- Makes informed inferences about compliance concerns
- Focuses on financial services regulatory requirements

## Key Banking Regulations Covered

- **FCA** (Financial Conduct Authority)
- **GDPR** (General Data Protection Regulation)
- **PCI DSS** (Payment Card Industry Data Security Standard)
- **Consumer Duty** (FCA Consumer Duty)
- **Fair Lending Laws** (Equal Credit Opportunity Act, Fair Housing Act)
- **AML/KYC** (Anti-Money Laundering / Know Your Customer)
- **Model Risk Management** (SR 11-7, SS1/23)

## Benefits

1. **Dual Purpose**: Operational banking + responsible AI oversight in one network
2. **Regulatory Readiness**: Built-in compliance evaluation framework
3. **Transparency**: Can demonstrate responsible AI practices to customers/regulators
4. **Risk Management**: Proactive identification of ethical and compliance issues
5. **Demo-Friendly**: Realistic responses without requiring live systems

## Next Steps

1. **Test the network**: `python -m run` and select `banking_ops_trust.hocon`
2. **Try operational queries**: Test standard banking interactions
3. **Try evaluation queries**: Request responsible AI assessments
4. **Customise pillars**: Add specific sub-agents to pillars as needed
5. **Integrate logging**: Connect to actual interaction logs for real evaluation

## Technical Notes

- Uses AAOSA (Agent as a Service Architecture) pattern
- Leverages `${aaosa_call}`, `${aaosa_command}`, `${aaosa_instructions}` from `aaosa.hocon`
- All agents in demo mode can simulate realistic banking scenarios
- TRUST agents focus on UK financial services regulations (can be adapted for other jurisdictions)


## How to Use
1. Start the server: python -m run
2. Select: banking_ops_trust.hocon from the network list
3. Try queries like:
- "I need a business loan for £50,000"
- "Evaluate the responsible AI compliance of our loan decision process"
- "How do you ensure fairness in fraud detection?"
- "Show me the transparency measures in our AI systems"

The TRUST BRAIN is accessible as a tool from the customer service representative, so you can seamlessly switch between operational banking and responsible AI evaluation queries! 🎯