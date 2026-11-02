"""The acts in the record (private build list)."""

# Whole Official Journal issues holding the consolidated Treaties (and the Charter).
TREATY_DOCS = [
    '11992M/TXT', '11992E/TXT', '11997M/TXT', '11997E/TXT', '12002M/TXT', '12002E/TXT', '12006M/TXT', '12006E/TXT',
    '12008M/TXT', '12008E/TXT', '12010M/TXT', '12010E/TXT', '12012M/TXT', '12012E/TXT', '12016M/TXT', '12016E/TXT',
    '12007P/TXT', '12010P/TXT', '12012P/TXT', '12016P/TXT',
]

# Base acts (CELEX) whose consolidated versions are recorded, most-used first.
BASES = [
    '32016R0679',  # GDPR
    '32022R2065',  # Digital Services Act
    '32022R1925',  # Digital Markets Act
    '32024R1689',  # AI Act
    '32014R0910',  # eIDAS
    '32012R1215',  # Brussels I bis
    '32008R0593',  # Rome I
    '32007R0864',  # Rome II
    '32004R0261',  # air passenger rights
    '32003R0001',  # competition rules (Art 101/102)
    '32004R0139',  # EU Merger Regulation
    '32015R0848',  # insolvency proceedings
    '32012R0650',  # succession
    '32017R1001',  # EU trade mark
    '32013R0604',  # Dublin III
    '32016R0399',  # Schengen Borders Code
    '32004R0883',  # social security coordination
    '32013R0952',  # Union Customs Code
    '32014R0596',  # Market Abuse Regulation
    '32017R1129',  # Prospectus Regulation
    '32012R0648',  # EMIR
    '32013R0575',  # Capital Requirements Regulation
    '32023R1114',  # MiCA
    '32022R2554',  # DORA
    '32018R1725',  # data protection by EU institutions
    '32019R2088',  # SFDR
    '32020R0852',  # Taxonomy Regulation
    '32006R1907',  # REACH
    '32011R0182',  # comitology
    '32001R1049',  # access to documents
    '31958R0001',  # language regime
    '32006L0112',  # VAT Directive
    '32011L0083',  # Consumer Rights Directive
    '32000L0031',  # e-Commerce Directive
    '32004L0038',  # citizens' free movement
    '31993L0013',  # unfair contract terms
    '32005L0029',  # unfair commercial practices
    '32015L2366',  # PSD2
    '32019L0790',  # copyright in the DSM
    '32001L0029',  # InfoSoc
    '32002L0058',  # ePrivacy
    '32014L0065',  # MiFID II
    '32013L0036',  # CRD
    '32009L0138',  # Solvency II
    '32003L0088',  # working time
    '32000L0078',  # equal treatment in employment
    '32000L0043',  # racial equality
    '32006L0054',  # gender equality (recast)
    '32006L0123',  # Services Directive
    '32014L0024',  # public procurement
    '32019L1937',  # whistleblowers
    '32022L2555',  # NIS2
    '32017L1132',  # company law
    '32015L0849',  # anti-money laundering (4th)
    '31985L0374',  # product liability
    '32016L0943',  # trade secrets
    '32004L0048',  # IP enforcement
    '31989L0391',  # OSH framework
    '32018L1972',  # European Electronic Communications Code
    '32010L0013',  # Audiovisual Media Services
    '32016L0680',  # Law Enforcement Directive
    '32008L0098',  # Waste Framework
    '32003L0087',  # EU ETS
    '32011L0092',  # EIA
    '31992L0043',  # Habitats
    '32009L0147',  # Birds
    '32000L0060',  # Water Framework
]

BASES += [
    '32014R0600',
    '32017R2402',
    '32014R0806',
    '32014L0059',
    '32009L0065',
    '32011L0061',
    '32015L2302',
    '32019L0770',
    '32019L0771',
    '32014L0017',
    '32020L1828',
    '32023L2225',
    '32019L1152',
    '32022L2041',
    '32008L0104',
    '31996L0071',
    '32001L0023',
    '31998L0059',
    '32019L1158',
    '32013L0034',
    '32024L1760',
    '32019L0944',
    '32018L2001',
    '32010L0075',
    '32008L0050',
    '32019L0882',
    '32023R2854',
    '32022R0868',
    '32019R0881',
    '32017R0745',
    '32002R0178',
    '32008R1272',
    '32011R1169',
    '32017R2394',
    '32023R0988',
    '32019R1020',
    '32019R1150',
    '32015R2120',
    '32022R0612',
    '32011R0492',
    '32019R1111',
    '32006R1896',
    '32007R0861',
    '32009R0004',
    '32017R1939',
    '32002F0584',
    '32021R0782',
    '32008R1008',
    '32019R0452',
    '32022R2560',
    '32021R0821',
    '32014R0651',
    '32022R0720',
    '32004R0726',
    '32001L0083',
    '32014R0536',
    '32009R1223',
    '32016L2341',
    '32017L0541',
    '32012L0029',
    '32013L0032',
    '32013L0033',
    '32011L0095',
    '32008L0115',
    '32003L0086',
    '32003L0109',
    '32021L1883',
    '32013R1308',
    '32018R0848',
]

# Folder names (act slugs) in the repository.
SLUGS = {
    '32016R0679': 'gdpr',
    '32022R2065': 'digital-services-act',
    '32022R1925': 'digital-markets-act',
    '32024R1689': 'ai-act',
    '32014R0910': 'eidas',
    '32012R1215': 'brussels-i-bis',
    '32008R0593': 'rome-i',
    '32007R0864': 'rome-ii',
    '32004R0261': 'air-passenger-rights',
    '32003R0001': 'antitrust-regulation',
    '32004R0139': 'merger-regulation',
    '32015R0848': 'insolvency-regulation',
    '32012R0650': 'succession-regulation',
    '32017R1001': 'eu-trade-mark-regulation',
    '32013R0604': 'dublin-iii',
    '32016R0399': 'schengen-borders-code',
    '32004R0883': 'social-security-coordination',
    '32013R0952': 'union-customs-code',
    '32014R0596': 'market-abuse-regulation',
    '32017R1129': 'prospectus-regulation',
    '32012R0648': 'emir',
    '32013R0575': 'capital-requirements-regulation',
    '32023R1114': 'mica',
    '32022R2554': 'dora',
    '32018R1725': 'eui-data-protection-regulation',
    '32019R2088': 'sfdr',
    '32020R0852': 'taxonomy-regulation',
    '32006R1907': 'reach',
    '32011R0182': 'comitology-regulation',
    '32001R1049': 'access-to-documents-regulation',
    '31958R0001': 'language-regulation',
    '32006L0112': 'vat-directive',
    '32011L0083': 'consumer-rights-directive',
    '32000L0031': 'e-commerce-directive',
    '32004L0038': 'free-movement-directive',
    '31993L0013': 'unfair-terms-directive',
    '32005L0029': 'unfair-commercial-practices-directive',
    '32015L2366': 'psd2',
    '32019L0790': 'dsm-copyright-directive',
    '32001L0029': 'infosoc-directive',
    '32002L0058': 'eprivacy-directive',
    '32014L0065': 'mifid-ii',
    '32013L0036': 'capital-requirements-directive',
    '32009L0138': 'solvency-ii',
    '32003L0088': 'working-time-directive',
    '32000L0078': 'employment-equality-directive',
    '32000L0043': 'racial-equality-directive',
    '32006L0054': 'gender-equality-directive',
    '32006L0123': 'services-directive',
    '32014L0024': 'public-procurement-directive',
    '32019L1937': 'whistleblower-directive',
    '32022L2555': 'nis2',
    '32017L1132': 'company-law-directive',
    '32015L0849': 'anti-money-laundering-directive',
    '31985L0374': 'product-liability-directive',
    '32016L0943': 'trade-secrets-directive',
    '32004L0048': 'ip-enforcement-directive',
    '31989L0391': 'osh-framework-directive',
    '32018L1972': 'electronic-communications-code',
    '32010L0013': 'audiovisual-media-services-directive',
    '32016L0680': 'law-enforcement-directive',
    '32008L0098': 'waste-framework-directive',
    '32003L0087': 'emissions-trading-directive',
    '32011L0092': 'eia-directive',
    '31992L0043': 'habitats-directive',
    '32009L0147': 'birds-directive',
    '32000L0060': 'water-framework-directive',
}
SLUGS.update({
    '32014R0600': 'mifir',
    '32017R2402': 'securitisation-regulation',
    '32014R0806': 'single-resolution-mechanism-regulation',
    '32014L0059': 'bank-recovery-and-resolution-directive',
    '32009L0065': 'ucits-directive',
    '32011L0061': 'aifmd',
    '32015L2302': 'package-travel-directive',
    '32019L0770': 'digital-content-directive',
    '32019L0771': 'sale-of-goods-directive',
    '32014L0017': 'mortgage-credit-directive',
    '32020L1828': 'representative-actions-directive',
    '32023L2225': 'consumer-credit-directive',
    '32019L1152': 'transparent-working-conditions-directive',
    '32022L2041': 'minimum-wages-directive',
    '32008L0104': 'temporary-agency-work-directive',
    '31996L0071': 'posting-of-workers-directive',
    '32001L0023': 'transfer-of-undertakings-directive',
    '31998L0059': 'collective-redundancies-directive',
    '32019L1158': 'work-life-balance-directive',
    '32013L0034': 'accounting-directive',
    '32024L1760': 'csddd',
    '32019L0944': 'electricity-directive',
    '32018L2001': 'renewable-energy-directive',
    '32010L0075': 'industrial-emissions-directive',
    '32008L0050': 'air-quality-directive',
    '32019L0882': 'european-accessibility-act',
    '32023R2854': 'data-act',
    '32022R0868': 'data-governance-act',
    '32019R0881': 'cybersecurity-act',
    '32017R0745': 'medical-devices-regulation',
    '32002R0178': 'general-food-law',
    '32008R1272': 'clp-regulation',
    '32011R1169': 'food-information-regulation',
    '32017R2394': 'consumer-protection-cooperation-regulation',
    '32023R0988': 'general-product-safety-regulation',
    '32019R1020': 'market-surveillance-regulation',
    '32019R1150': 'platform-to-business-regulation',
    '32015R2120': 'open-internet-regulation',
    '32022R0612': 'roaming-regulation',
    '32011R0492': 'workers-free-movement-regulation',
    '32019R1111': 'brussels-iib',
    '32006R1896': 'european-order-for-payment',
    '32007R0861': 'european-small-claims',
    '32009R0004': 'maintenance-regulation',
    '32017R1939': 'eppo-regulation',
    '32002F0584': 'european-arrest-warrant',
    '32021R0782': 'rail-passenger-rights',
    '32008R1008': 'air-services-regulation',
    '32019R0452': 'fdi-screening-regulation',
    '32022R2560': 'foreign-subsidies-regulation',
    '32021R0821': 'dual-use-regulation',
    '32014R0651': 'general-block-exemption-regulation',
    '32022R0720': 'vertical-block-exemption-regulation',
    '32004R0726': 'medicines-regulation',
    '32001L0083': 'medicinal-products-directive',
    '32014R0536': 'clinical-trials-regulation',
    '32009R1223': 'cosmetics-regulation',
    '32016L2341': 'iorp-ii',
    '32017L0541': 'terrorism-directive',
    '32012L0029': 'victims-rights-directive',
    '32013L0032': 'asylum-procedures-directive',
    '32013L0033': 'reception-conditions-directive',
    '32011L0095': 'qualification-directive',
    '32008L0115': 'return-directive',
    '32003L0086': 'family-reunification-directive',
    '32003L0109': 'long-term-residents-directive',
    '32021L1883': 'blue-card-directive',
    '32013R1308': 'cmo-regulation',
    '32018R0848': 'organic-production-regulation',
})
