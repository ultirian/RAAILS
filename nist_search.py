#!/usr/bin/env python3

"""Calls on NIST API to search for CVEs by CPE name, Additional fields have been parsed out 
but not yet implemented"""

import json
import requests
import table_generator as tg
__author__ = 'Chris Weaver'
__version__ = '0.0.7'
__license__ = 'MIT'

# API_KEY = "674ce019-fd0d-481f-8468-10ca5e2f0cb4"

def search_by_cpe_name(cpename_in):
    """Searches NIST API for CVEs by CPE name"""

    API_KEY = "674ce019-fd0d-481f-8468-10ca5e2f0cb4"

    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    params = {"cpeName": cpename_in, "resultsPerPage": 1}
    headers = {"api_key": API_KEY}

    response = requests.get(url, params=params, headers=headers, timeout=10)

    print(response)

    if response.status_code == 200:
        data = response.json()

        # Do something with the response data
        resultsPerPage = data['resultsPerPage']
        startIndex = data['startIndex']
        totalResults = data['totalResults']
        format = data['format']
        version = data['version']
        timestamp = data['timestamp']

        vulnerabilities = data['vulnerabilities']
        for vulnerability in vulnerabilities:
            cve = vulnerability['cve']
            id = cve['id']
            sourceIdentifier = cve['sourceIdentifier']
            published = cve['published']
            lastModified = cve['lastModified']
            vulnStatus = cve['vulnStatus']
            # cisaExploitAdd = cve['cisaExploitAdd']
            # cisaActionDue = cve['cisaActionDue']
            # cisaRequiredAction = cve['cisaRequiredAction']
            # cisaVulnerabilityName = cve['cisaVulnerabilityName']

            descriptions = cve['descriptions']
            english = descriptions[0]
            description_english_value = english['value']
            #for description in descriptions:
            #    lang = description['lang']
            #    value = description['value']

            metrics = cve['metrics']
            cvssMetricV2 = metrics['cvssMetricV2']
            for cvss in cvssMetricV2:
                source = cvss['source']
                type = cvss['type']
                cvssData = cvss['cvssData']
                version = cvssData['version']
                vectorString = cvssData['vectorString']
                accessVector = cvssData['accessVector']
                accessComplexity = cvssData['accessComplexity']
                authentication = cvssData['authentication']
                confidentialityImpact = cvssData['confidentialityImpact']
                integrityImpact = cvssData['integrityImpact']
                availabilityImpact = cvssData['availabilityImpact']
                baseScore = cvssData['baseScore']

            weaknesses = cve['weaknesses']
            for weakness in weaknesses:
                source = weakness['source']
                type = weakness['type']
                description = weakness['description']
                for desc in description:
                    lang = desc['lang']
                    value = desc['value']

            configurations = cve['configurations']
            for configuration in configurations:
                nodes = configuration['nodes']
                for node in nodes:
                    operator = node['operator']
                    negate = node['negate']
                    cpeMatch = node['cpeMatch']
                    for cpe in cpeMatch:
                        vulnerable = cpe['vulnerable']
                        criteria = cpe['criteria']
                        matchCriteriaId = cpe['matchCriteriaId']

        # print(description_english_value)
        # print(id)
        # print(baseScore)

        cve_id_list = [id]
        baseScore_list = [baseScore]
        description_english_value_list = [description_english_value]
        # python sees basescore as float so needs converstion to str.
        tg.print_nist_tables(cve_id_list, baseScore_list, description_english_value_list)

        search_by_cve(id)

    else:
        print(f"Error: {response.status_code} - {response.reason}")

def search_by_cve(cve_id):
    """Searches NIST API for CVEs by CVE ID"""
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}&resultsPerPage=1"
    response = requests.get(url, timeout=10)
    if response.ok:
        data = json.loads(response.content)
        if data.get('result'):
            return data['result'][0]
    return None
