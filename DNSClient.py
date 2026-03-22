import dns.resolver

local_host_ip = "127.0.0.1"
real_name_server = "8.8.8.8"

domainList = ['example.com.', 'safebank.com.', 'google.com.', 'nyu.edu.', 'legitsite.com.']

def query_local_dns_server(domain_name, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [local_host_ip]
    answer = resolver.resolve(domain_name, question_type)
    return answer[0].to_text()

def query_dns_server(domain_name, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [real_name_server]
    answer = resolver.resolve(domain_name, question_type)
    return answer[0].to_text()

def compare_dns_servers(domainList, question_type):
    for domain in domainList:
        local_ip = query_local_dns_server(domain, question_type)
        public_ip = query_dns_server(domain, question_type)
        if local_ip != public_ip:
            return False
    return True

def local_external_DNS_output(question_type):
    print("Local DNS:")
    for domain in domainList:
        print(domain, query_local_dns_server(domain, question_type))

    print("\nPublic DNS:")
    for domain in domainList:
        print(domain, query_dns_server(domain, question_type))

def exfiltrate_info(domain_name, question_type):
    return query_local_dns_server(domain_name, question_type)

if __name__ == "__main__":
    question_type = 'A'
    result = compare_dns_servers(domainList, question_type)
    print("Match:", result)
    print(query_local_dns_server('nyu.edu.', question_type))
