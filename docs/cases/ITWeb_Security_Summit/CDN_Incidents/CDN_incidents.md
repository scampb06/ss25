# European Counter Disinformation Network Incidents

## Methdology

All CDN Incident Alerts were combined into file `Alerts.pdf`. Perplexity did a first-pass to apply the attached incident template to incidents in `Alerts.pdf` that appear to be strong or plausible hybrid cyber/FIMI candidates. Entries were drafted from the PDF text alone, without yet following the `Report` hyperlink. Where the PDF alone appeared unlikely to satisfy the 25% completeness rule, fields were marked `not enough info` pending linked-report follow-up

Then a final pass improved several borderline entries, especially the RT Deutsch mirror/content-laundering cases and the WABEO entry, by adding archive evidence of continued sanctions-evasion behavior, newer RT Germany distribution assets, and WABEO's own framing of an app-based “court-proof” vote observation model. Some gaps remain, however: for WABEO there is still limited public detail on app security, data validation, and governance; for the RT mirror ecosystem, the technical picture is stronger than the public attribution picture. These cases are now better grounded, but they should still be presented as medium-confidence hybrid cases rather than the strongest exemplars in the set.

---

## Incident Summary

**Title:** Operation Overload targeting fact-checkers and media  
**Date:** August 2023 to May 2024  
**Targets:** Fact-checkers, newsrooms, researchers, and broader Western information environments, especially in France and Germany  
**Perpetrator:** Actors aligned with Russian interests  
**Motivation:** Overwhelm verification actors, deplete their resources, and propagate pro-Kremlin narratives

## Cyberattack Details

- **Nature:** Coordinated email campaign, platform manipulation, AI-generated profiles, and automated account creation supporting influence activity
- **Systems Attacked:** Email channels of media and fact-checking organizations; X, Telegram, VKontakte/Odnoklassniki spillover, and Kremlin-aligned website ecosystems including the Pravda network
- **Data Held:** Manipulated videos, images, fake article screenshots, counterfeit Instagram-story style visuals, email lures, and links to Telegram, X, and pro-Russian websites
- **Availability Impact:** No classic outage reported, but the operation aimed to overload verification capacity and consume newsroom time and attention
- **Data Exfiltration/Alteration:** No confirmed exfiltration described in the report; the campaign focused on delivering manipulated content and systematically created sender assets
- **Estimated Impact:** The June 2024 report documented over 800 targeted organizations, more than 200 collected emails, over 250 manipulated content items, and around 100 inauthentic X accounts; the September 2024 update raised the estimate to around 71,000 emails sent to nearly 250 organizations
- **Investigators:** CheckFirst, Reset.Tech, EU DisinfoLab partner organizations, and collaborating fact-checking outlets
- **Remediation:** Suspicious emails and content reported; increased coordination among fact-checkers and journalists; investment in detection tools, media-forensics workflows, and public-awareness measures recommended

## Disinformation Details

- **Nature:** Coordinated disinformation campaign using manipulated multimedia, content amalgamation, and cross-platform amplification
- **Narratives:** Anti-Ukraine and anti-Macron narratives
- **Deception:** Fake citizen personas using mostly Gmail accounts, content amalgamation across multiple media formats, impersonation of reputable media brands and public figures, and coordinated seeding on Telegram before amplification on X and aligned websites
- **Platforms:** Email, Telegram, X, Kremlin-aligned websites, and in some cases other Russian social platforms
- **Reach:** The initial report documented targeting of over 800 organizations; the later update estimated around 71,000 emails to nearly 250 organizations worldwide
- **Impact:** Heightened anxiety, distrust, wasted verification resources, and increased likelihood that false narratives would spread through debunks or media attention
- **Disinfo Investigators:** CheckFirst, Reset.Tech, EU DisinfoLab partners, and targeted fact-checking and media organizations
- **Remediation:** Reporting to platforms, inter-organizational coordination, better detection tooling, archiving, and public education
- **Link to Cyberattack:** The operation used technical email delivery, coordinated fake accounts, and cross-platform digital infrastructure to manufacture the appearance of virality and push targets into amplifying fabricated stories

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0003, pp. 5-6  
[2](https://checkfirst.network/wp-content/uploads/2024/06/Operation_Overload_WEB.pdf): CheckFirst / Reset.Tech, *Operation Overload* (June 2024)  
[3](https://checkfirst.network/operation-overload-a-growing-disinformation-threat-now-targeting-the-u-s-presidential-election/): CheckFirst, Operation Overload update (September 2024)  

---

## Incident Summary

**Title:** Doppelganger influence operation on X and Facebook ads  
**Date:** June 4 to August 23, 2024  
**Targets:** EU member state audiences, especially France, Germany, Poland, and Italy; support for Ukraine  
**Perpetrator:** Russian influence operation Doppelganger  
**Motivation:** Undermine support for Ukraine, polarize public debate, and discourage targeted countries from supporting Ukraine

## Cyberattack Details

- **Nature:** Coordinated inauthentic accounts, redirect infrastructure, and targeted advertising across platforms
- **Systems Attacked:** X posting ecosystem, Meta advertising systems, redirect URL infrastructure
- **Data Held:** Operational posts, redirect links, and targeted ad content
- **Availability Impact:** No major outage reported
- **Data Exfiltration/Alteration:** Not enough info on exfiltration; operation relied on deceptive distribution infrastructure
- **Estimated Impact:** 1,366 inauthentic X posts and 98 Facebook ads with combined views above 4.6 million by end of June
- **Investigators:** Civil society organizations and European Commission alerts referenced in the PDF
- **Remediation:** X was alerted and had not responded at the time of writing; Meta was informed and associated Facebook ad pages were taken down or no longer in use

## Disinformation Details

- **Nature:** Coordinated inauthentic behavior spreading pro-Russian narratives and redirecting users to operational content
- **Narratives:** Cease Ukraine support; discredit Western governments and political parties; support pro-Russian parties; polarizing economic and inflation narratives
- **Deception:** Inauthentic accounts posing as authentic users, coordinated replies, redirect links, and unlabeled targeted political ads
- **Platforms:** X and Meta
- **Reach:** Combined views exceeded 4.6 million according to X data
- **Impact:** Polarization in targeted countries and erosion of support for Ukraine
- **Disinfo Investigators:** Alliance4Europe, CeMAS, FDD, BIQdata.pl/Gazeta Wyborcza, Science Feedback, and other contributors listed in the alert
- **Remediation:** Reporting to platforms and EU institutions; continued monitoring of Doppelganger tactics and techniques
- **Link to Cyberattack:** The influence campaign used technical redirect infrastructure and coordinated platform abuse to route users toward operational content and targeted messaging

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0027, pp. 21-22  

---

## Incident Summary

**Title:** Doppelganger coordinated inauthentic behavior network on X continued in August 2024  
**Date:** August 1 to August 16, 2024  
**Targets:** German-language audiences on X; support for Ukraine; German trust in government and Western alliances  
**Perpetrator:** Highly likely part of the Russian Doppelganger campaign  
**Motivation:** Decrease support for Ukraine and sow distrust in the German government and Western allies

## Cyberattack Details

- **Nature:** Coordinated publication, likely automation, FIKED redirects, and front-link infrastructure
- **Systems Attacked:** X posting and reply ecosystem; redirect chains to Doppelganger articles and generic destinations
- **Data Held:** Inauthentic posts, redirect URLs, authentic and fabricated articles, images, and videos
- **Availability Impact:** No major outage reported
- **Data Exfiltration/Alteration:** Not enough info on exfiltration; technical abuse centered on redirects and posting coordination
- **Estimated Impact:** 104 German-language pro-Russian posts reached more than 710,000 combined views by mid-August, with 78 still online by September 6
- **Investigators:** CeMAS, Alliance4Europe, CDN, and prior DFRLab attribution are referenced in the alert
- **Remediation:** Reported to X, EU institutions, and German representatives; wider public report planned

## Disinformation Details

- **Nature:** Coordinated inauthentic posting and reply amplification using multiple behavioral patterns
- **Narratives:** Cease Ukraine support; anti-government themes; criticism of support for Ukraine and Western alliances
- **Deception:** Accounts posing as authentic users, synchronous posting, front links, and redirect chains to Doppelganger content
- **Platforms:** X
- **Reach:** More than 710,000 combined views by mid-August 2024
- **Impact:** Low direct engagement but significant visibility and persistent presence on the platform
- **Disinfo Investigators:** CeMAS and associated researchers cited in the alert
- **Remediation:** Platform reporting, public exposure, and recommendation that X implement systematic pattern recognition
- **Link to Cyberattack:** The operation depended on technical redirect infrastructure and coordinated account behavior to amplify influence content at scale

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0028, p. 27  

---

## Incident Summary

**Title:** Operation Overload activity update, September 2024  
**Date:** January to September 2024  
**Targets:** Newsrooms, fact-checkers, researchers, civil society organizations, and journalists  
**Perpetrator:** Operation Overload, linked in the alert to Russia  
**Motivation:** Waste target resources, deceive intermediaries into spreading false narratives, and support Kremlin interests

## Cyberattack Details

- **Nature:** Mass disinformation email distribution combined with impersonation and AI-assisted deceptive content
- **Systems Attacked:** Email systems of researchers, media, and fact-checking organizations; online distribution channels on X and Telegram; associated pro-Russian websites in the Pravda ecosystem
- **Data Held:** False news stories, doctored images, manipulated graffiti photos, fabricated social media posts, fake media covers, and AI-generated or deceptively edited audio content
- **Availability Impact:** No service outage reported, but severe resource drain on recipients and the risk of newsroom workflow disruption
- **Data Exfiltration/Alteration:** No confirmed data theft described in the available materials; the campaign centered on sustained content injection and impersonation
- **Estimated Impact:** Around 71,000 disinformation emails sent to roughly 245 organizations by September 2024, with strong expansion during the Paris Olympics and added targeting of the U.S. election
- **Investigators:** CheckFirst, Reset.Tech, and associated researchers and partner organizations
- **Remediation:** Alerts sent to EU institutions, governments, civil society organizations, and journalists; ongoing monitoring and exposure of newly evolving TTPs

## Disinformation Details

- **Nature:** Coordinated impersonation and multimedia disinformation campaign exploiting major events and public anxiety
- **Narratives:** Paris Olympics are unsafe and mismanaged; economic instability in France; anti-Ukrainian narratives; rumors harming Kamala Harris; discrediting military aid to Ukraine
- **Deception:** AI-generated or deceptively edited audio, impersonated Western news outlets, fake TikTok-style videos, fake newspaper and magazine covers, QR-code engagement hooks, and fabricated media and social posts
- **Platforms:** Email, X, Telegram, and pro-Russian websites
- **Reach:** Nearly 250 organizations received emails according to the September 2024 update, and the campaign increasingly targeted U.S. political narratives as well as France and Germany
- **Impact:** Flooding of verification organizations, broad risk of false amplification in public discourse, and expansion of Kremlin-aligned narratives into major event and election cycles
- **Disinfo Investigators:** CheckFirst, Reset.Tech, and partner organizations
- **Remediation:** Alerting institutions and journalists; continued tracking of evolving formats and downstream amplification
- **Link to Cyberattack:** The influence operation used email infrastructure, impersonation of trusted brands, and digitally manipulated artifacts as its core delivery and scaling mechanism

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0029, p. 29  
[2](https://checkfirst.network/operation-overload-a-growing-disinformation-threat-now-targeting-the-u-s-presidential-election/): CheckFirst, Operation Overload update (September 2024)  
[3](https://checkfirst.network/wp-content/uploads/2024/06/Operation_Overload_WEB.pdf): CheckFirst / Reset.Tech, *Operation Overload* (June 2024)  

---

## Incident Summary

**Title:** German Doppelganger activity remains on X months after publication  
**Date:** November 24, 2023 to March 31, 2024, with status check on November 21, 2024  
**Targets:** German audiences, support for Ukraine, trust in the German government and Western alliances  
**Perpetrator:** Russian influence campaign Doppelganger  
**Motivation:** Decrease support for Ukraine, sow distrust in government, and cultivate support for pro-Russian parties

## Cyberattack Details

- **Nature:** Redirect URLs, shortened URLs, repetitive text/image/video patterns, and infrastructure variations tied to known Doppelganger domains
- **Systems Attacked:** X posting ecosystem and redirect infrastructure routing to influence content
- **Data Held:** 666 posts, shortened URLs, images, videos, and operational content linked to known domains
- **Availability Impact:** No major outage reported
- **Data Exfiltration/Alteration:** Not enough info on exfiltration; abuse focused on delivery and concealment infrastructure
- **Estimated Impact:** Nearly 920,000 views by mid-August 2024; 592 of 666 posts remained available in November 2024
- **Investigators:** CeMAS, German MFA, CDN, DFRLab, Qurium, HarfangLab, and Sekoia are cited in the alert
- **Remediation:** Recommendation that X identify and mitigate similar posts and future Doppelganger activity

## Disinformation Details

- **Nature:** Coordinated inauthentic posting with redirect links and pro-Russian political narratives
- **Narratives:** Cease Ukraine support; anti-government; economic decline; support for pro-Russian parties such as AfD and BSW
- **Deception:** Accounts posing as authentic users, repeated posting formulas, redirect links, and concealed network identity
- **Platforms:** X
- **Reach:** Nearly 920,000 views according to X data
- **Impact:** Persistent low-friction exposure of pro-Russian narratives in German political discourse
- **Disinfo Investigators:** CeMAS and partner researchers cited in the alert
- **Remediation:** Reporting to X and continued monitoring of account and URL patterns
- **Link to Cyberattack:** The influence activity depended on redirect infrastructure and technical URL concealment to circulate operational content while evading moderation

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0032, pp. 32-33  

---

## Incident Summary

**Title:** Illegal Russian influence operations continue despite sanctions  
**Date:** November 3 to December 4, 2024  
**Targets:** EU member state governments, Ukraine, and opinion on U.S. support for Israel and Ukraine  
**Perpetrator:** Doppelganger operator SDA, according to the alert  
**Motivation:** Smear governments, discourage support for Ukraine, and exploit geopolitical fractures involving Israel and Europe

## Cyberattack Details

- **Nature:** Geolocation-based redirects, front domains, shared IP infrastructure, and new Doppelganger domains
- **Systems Attacked:** X posting ecosystem and domain infrastructure linked to operational content
- **Data Held:** 959 tweets, front domains, redirect mechanisms, and related visual and text content
- **Availability Impact:** No major outage reported
- **Data Exfiltration/Alteration:** Not enough info on exfiltration; operation centered on URL redirection and domain abuse
- **Estimated Impact:** 4,135,274 views according to X API data, though the alert notes reliability issues
- **Investigators:** Alliance4Europe and CeMAS contributors listed in the alert
- **Remediation:** Alert sent to X and European governments; recommendation that X address systemic risk and that sanctions implications be investigated

## Disinformation Details

- **Nature:** Continued coordinated influence operation using quote-posts, redirects, and look-alike domains
- **Narratives:** Russia perceives Ukraine’s use of U.S. weapons against its territory as direct attack by the United States; calls for a cease-fire in Ukraine and peace negotiations; support for Israel; fear among European Jews; calls for protests against European governments
- **Deception:** Concealed network identity, redirect URLs, domain assets, and inauthentic comment amplification
- **Platforms:** X
- **Reach:** Over 4.1 million views according to the platform API
- **Impact:** Sustained visibility of illegal or sanction-breaching influence activity despite prior reporting
- **Disinfo Investigators:** Alliance4Europe and CeMAS contributors
- **Remediation:** Reporting to X and governments; call for broader sanctions and DSA investigation
- **Link to Cyberattack:** The campaign’s influence effects rely on reusable technical infrastructure—front domains, redirects, and shared IPs—that route users to operational content and help evade enforcement

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0037, p. 37  

---

## Incident Summary

**Title:** Doppelganger continues operations in German, French, Hebrew, and Ukrainian  
**Date:** December 28, 2023 to January 5, 2024  
**Targets:** EU states, Ukraine, Israel, and the United States in multiple language environments  
**Perpetrator:** Likely parts of Operation Doppelganger; producer identified in the alert as SDA  
**Motivation:** Smear governments, divide alliances, and undermine trust between the EU, U.S., Ukraine, and Israel

## Cyberattack Details

- **Nature:** Fake articles, look-alike domains, redirect infrastructure, and common Russian IP back-end hosting
- **Systems Attacked:** X dissemination ecosystem and spoofed domain infrastructure
- **Data Held:** 288 tweets, 24 fake articles, and multiple operational domains
- **Availability Impact:** No major outage reported
- **Data Exfiltration/Alteration:** Not enough info on exfiltration; principal technical feature was domain and redirect abuse
- **Estimated Impact:** 1,200,638 views according to X API data, with reliability caveat noted in the alert
- **Investigators:** Alliance4Europe and other named contributors in the alert
- **Remediation:** Alert spoofed platforms, notify governments and X, and investigate the UK entity linked to the IP infrastructure

## Disinformation Details

- **Nature:** Multilingual coordinated influence activity using fake articles and impersonation-style web assets
- **Narratives:** Macron has led France to ruin; Germany is being impoverished; sanctions hurt Germany; Israel is weakened and to blame for domestic problems; U.S. foreign policy is antisemitic; Ukraine is corrupt and losing the war
- **Deception:** Spoofed and look-alike domains, fake articles, redirect links, and concealed network identity
- **Platforms:** X
- **Reach:** About 1.2 million views according to X API data
- **Impact:** Multi-country narrative laundering across several sensitive geopolitical topics
- **Disinfo Investigators:** Alliance4Europe contributors listed in the alert
- **Remediation:** Spoofed platforms alerted; recommendation to investigate Partner Hosting LTD
- **Link to Cyberattack:** The influence effort depended on deceptive domains, back-end hosting, and technical redirects to launder content and give it false legitimacy

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0038, pp. 38-39  

---

## Incident Summary

**Title:** Georgescu’s unexpected win and algorithmic manipulation on TikTok  
**Date:** Romanian presidential election first round, November 24, 2024  
**Targets:** Romanian presidential election, Romanian voters, and TikTok’s recommendation environment  
**Perpetrator:** Coordinated TikTok campaign likely organized via Telegram groups and incentivized user participation  
**Motivation:** Cultivate support for Calin Georgescu and manipulate the TikTok algorithm to amplify his campaign

## Cyberattack Details

- **Nature:** Coordinated flooding of TikTok information space, algorithm gaming, and Telegram-based orchestration
- **Systems Attacked:** TikTok recommendation and content-ranking systems; Telegram coordination channels
- **Data Held:** Hashtag-driven campaign content, competition mechanisms, and repost instructions
- **Availability Impact:** No outage reported
- **Data Exfiltration/Alteration:** No confirmed exfiltration; focus was on algorithmic manipulation and deceptive amplification
- **Estimated Impact:** Georgescu’s account gained over 150 million views in two months according to the alert
- **Investigators:** Alliance4Europe, Romanian civil society, and Expert Forum are referenced in the alert
- **Remediation:** Establish connections with Romanian civil society and regulators; TikTok should investigate coordinated inauthentic activity and Telegram channels used for coordination

## Disinformation Details

- **Nature:** Coordinated inauthentic campaign using influencer amplification, hashtags, and contests to flood TikTok
- **Narratives:** Support for Calin Georgescu presented through themes of neutrality and economic independence
- **Deception:** Concealed coordination, hidden affiliations, and possible use of contests and prizes to spur amplification
- **Platforms:** Telegram and TikTok
- **Reach:** Very high; the alert cites over 150 million views in two months
- **Impact:** Major boost to candidate visibility and possible distortion of the election information environment
- **Disinfo Investigators:** Alliance4Europe, Romanian civil society, and Expert Forum
- **Remediation:** Platform investigation, publication of results, and investigation of Telegram coordination channels
- **Link to Cyberattack:** The influence effort used coordinated technical manipulation of TikTok’s ranking and recommendation systems rather than a conventional network intrusion

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0040, p. 40  

---

## Incident Summary

**Title:** Russian influence operation Doppelganger expands to Bluesky  
**Date:** January 17 to January 24, 2025  
**Targets:** German audiences on Bluesky and, more broadly, users in English, Polish, French, and Turkish  
**Perpetrator:** Russian Doppelganger influence operation  
**Motivation:** Discredit Ukraine and the German traffic-light coalition and test or extend influence tradecraft onto Bluesky

## Cyberattack Details

- **Nature:** Bulk-created asset network, coordinated reply posting, and account activation patterns
- **Systems Attacked:** Bluesky social interaction and reply systems
- **Data Held:** More than 100 German-language accounts and over 4,900 posts
- **Availability Impact:** No outage reported
- **Data Exfiltration/Alteration:** Not enough info on exfiltration; operation centered on coordinated account behavior
- **Estimated Impact:** Limited direct impact so far, but 4,300 posts were produced by a second batch of accounts posting hundreds of replies daily
- **Investigators:** Alliance4Europe and independent contributors cited in the alert
- **Remediation:** Reported to Bluesky, journalists, and European governments; recommendation that Bluesky use known Doppelganger behavior patterns to mitigate the operation

## Disinformation Details

- **Nature:** Coordinated inauthentic social media commenting using local personas and concealed sponsorship
- **Narratives:** Economic and political decline in Germany and Europe; criticism of political leadership; opposition to German foreign policy; U.S. exploitation of Germany and the EU
- **Deception:** Local personas, bulk-created assets, concealed sponsorship, and inauthentic comment campaigns
- **Platforms:** Bluesky
- **Reach:** Likely limited; 667 posts in one batch and 4,300 in another, with no meaningful interaction at the time of review
- **Impact:** Early-stage platform penetration by a known Russian influence operation
- **Disinfo Investigators:** Alliance4Europe and independent contributors named in the alert
- **Remediation:** Platform reporting and continued monitoring
- **Link to Cyberattack:** The campaign relies on technical account creation patterns and coordinated posting infrastructure to transplant known influence tactics onto a new platform

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0041, p. 41  

---

## Incident Summary

**Title:** Doppelganger continues on X with new domains and sharing authentic articles  
**Date:** January 9 to January 19, 2025  
**Targets:** German election audiences, Ukraine-related discourse, and German concerns about the economy  
**Perpetrator:** Russian influence operation Doppelganger  
**Motivation:** Cause concerns around financial issues in Germany, smear the government and Ukraine, and adapt the campaign for the German election context

## Cyberattack Details

- **Nature:** Use of new operational domains, look-alike domains, redirects, and repurposing of authentic articles
- **Systems Attacked:** X dissemination ecosystem and spoofed web infrastructure
- **Data Held:** 573 tweets, authentic and fabricated articles, redirect pathways, and domain portfolio
- **Availability Impact:** No outage reported
- **Data Exfiltration/Alteration:** Not enough info on exfiltration; operation focused on infrastructure abuse and deceptive republishing
- **Estimated Impact:** 1,627,968 views according to the alert
- **Investigators:** Joel Haglund and Alliance4Europe, with earlier comparisons to prior Doppelganger monitoring
- **Remediation:** Report all tweets and involved accounts to EU authorities and X

## Disinformation Details

- **Nature:** Coordinated propaganda using both authentic and fabricated articles framed for operational purposes
- **Narratives:** German economic weakness; failing companies; irresponsible banks; labor shortages; declining demand for electric vehicles; Ukraine is losing
- **Deception:** Look-alike domains, development of fake news, deceptive framing of authentic articles, and redirect infrastructure
- **Platforms:** X
- **Reach:** About 1.63 million views according to Twitter API data cited in the alert
- **Impact:** Narrative laundering through mixed authentic and inauthentic content
- **Disinfo Investigators:** Alliance4Europe and earlier external researchers cited in the alert
- **Remediation:** Reporting to EU authorities and X
- **Link to Cyberattack:** The operation fuses influence messaging with technical domain infrastructure and redirects that disguise origin and route users to operational content

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0042, pp. 42-43  

---

## Incident Summary

**Title:** Coordinated and verified pro-Kremlin campaign published hundreds of posts on X  
**Date:** December 20, 2024 to January 21, 2025  
**Targets:** German audiences, the German election, and support for Ukraine  
**Perpetrator:** Inauthentic pro-Kremlin accounts on X documented by CeMAS  
**Motivation:** Create division in German society, degrade support for Ukraine, and promote parties aligned with pro-Kremlin positions

## Cyberattack Details

- **Nature:** Coordinated inauthentic posting with verified accounts and hashtag hijacking
- **Systems Attacked:** X trend and distribution ecosystem
- **Data Held:** 563 German-language posts from 18 accounts, of which 15 had X verification checkmarks
- **Availability Impact:** No outage reported
- **Data Exfiltration/Alteration:** No confirmed exfiltration in the alert
- **Estimated Impact:** 191,681 views by January 22, 2025
- **Investigators:** CeMAS and Reset Tech are referenced in the alert history
- **Remediation:** Reported to X, the European Commission, and German authorities; recommendation that X improve proactive CIB detection

## Disinformation Details

- **Nature:** Coordinated inauthentic campaign using existing hashtags and verified accounts to boost visibility
- **Narratives:** Sanctions against Russia are ineffective and harmful; Ukraine is inferior or defeated; Germany suffers from supporting Ukraine; Germany should pursue peace negotiations without Ukraine; support for AfD and BSW
- **Deception:** Inauthentic accounts, video and image reuse, verified accounts providing more favorable distribution conditions, and hijacked trending hashtags
- **Platforms:** X
- **Reach:** 191,681 views by January 22, 2025
- **Impact:** Limited immediate real-life impact but persistent penetration of German election discourse
- **Disinfo Investigators:** CeMAS
- **Remediation:** Reporting to X and authorities; stronger platform detection of malicious verified accounts
- **Link to Cyberattack:** The campaign exploits platform distribution mechanics and account verification infrastructure to amplify coordinated influence content

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0043, pp. 43-44  

---

## Incident Summary

**Title:** Storm-1516 and R-FBI Russian attempts to interfere in the German election  
**Date:** November 5, 2024 to February 9, 2025  
**Targets:** German election candidates, parties, voters, and public trust in the election process  
**Perpetrator:** Russian influence operations Storm-1516 and the Foundation to Battle Injustice (R-FBI)  
**Motivation:** Defame political targets, interfere in the German election, and feed polarization in German society

## Cyberattack Details

- **Nature:** Fabricated articles, fake news sites, deepfakes, cross-platform amplification, and influencer baiting
- **Systems Attacked:** News and social media ecosystems spanning X, Meta, Telegram, and TikTok
- **Data Held:** At least 12 German-language narratives in article and video form, plus supporting inauthentic site infrastructure
- **Availability Impact:** No service outage reported
- **Data Exfiltration/Alteration:** Not enough info on exfiltration; campaign relied on synthetic and deceptive content creation
- **Estimated Impact:** At least 25 million views and 5,610 interactions on the posts according to the alert
- **Investigators:** CeMAS, Alliance4Europe, and independent contributors listed in the alert
- **Remediation:** Case flagged to EU and German authorities and social media platforms; recommendation to raise awareness to avoid unintentional amplification

## Disinformation Details

- **Nature:** Election interference campaign using fake articles, manipulated videos, and platform-spanning amplification
- **Narratives:** Discredit anti-Russian and governing parties; accuse politicians of abuse, paedophilia, and corruption; depict Ukraine supporters as undermining Germany; portray Ukrainian government as corrupt or Nazi
- **Deception:** Creation of inauthentic news sites, AI-generated videos or deepfakes, and baiting influencers to spread content
- **Platforms:** X, Meta, Telegram, and TikTok
- **Reach:** At least 25 million views according to Telegram and TikTok metrics cited in the alert
- **Impact:** Broad election-focused narrative pollution with possible manipulated engagement metrics
- **Disinfo Investigators:** CeMAS, Alliance4Europe, and named contributors in the alert
- **Remediation:** Platform and government notification; public awareness to reduce amplification
- **Link to Cyberattack:** The campaign depends on technical creation of fake news infrastructure and manipulated multimedia to give false stories credibility and scale

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0044, p. 44  

---

## Incident Summary

**Title:** Coordinated disinformation network uses AI and media impersonation to target the German election  
**Date:** January 1 to January 31, 2025  
**Targets:** German election discourse, German politicians, government agencies, academic institutions, and journalists  
**Perpetrator:** Pro-Kremlin influence operation Operation Overload  
**Motivation:** Discredit politicians, divide users, harass institutions, and mislead audiences about the German election

## Cyberattack Details

- **Nature:** Coordinated X network, AI-manipulated audio, branded impersonation of legitimate organizations, and synchronized amplification by more than 6,000 bot accounts
- **Systems Attacked:** X posting, reposting, and tagging ecosystem; trust associated with news and institutional brands
- **Data Held:** 33 unique videos, 48 coordinating accounts, and a larger amplifier network
- **Availability Impact:** No outage reported
- **Data Exfiltration/Alteration:** Not enough info on exfiltration; core tactic was manipulated video and synchronized distribution
- **Estimated Impact:** Original network had limited engagement, but the 48 accounts collectively garnered 2.5 million views averaging 52,480 per post
- **Investigators:** Institute for Strategic Dialogue and associated monitors
- **Remediation:** Contact regulators, news outlets, and institutions targeted by impersonation to increase awareness and trigger further action

## Disinformation Details

- **Nature:** Coordinated election disinformation campaign using spoofed branding and manipulated media
- **Narratives:** The election is unsafe due to threats; individual politicians are corrupt or cannot be trusted; Ukrainian refugees threaten German society; support for Ukraine exposes Germany to Russian attack
- **Deception:** Co-opted trusted sources, AI-generated audio, impersonation of DW, Sky News, government agencies, and academic institutions, and bot amplification
- **Platforms:** X
- **Reach:** 2.5 million views across 48 identified accounts; more than 10,597 shares from coordinated amplifiers
- **Impact:** Limited organic uptake but substantial synthetic amplification and credibility risk for impersonated institutions
- **Disinfo Investigators:** Institute for Strategic Dialogue
- **Remediation:** Regulator engagement, outreach to news outlets and institutions, and broader monitoring
- **Link to Cyberattack:** The operation fuses technical media manipulation, impersonation infrastructure, and bot-driven amplification with election-focused influence narratives

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0046, pp. 46-47  

---

## Incident Summary

**Title:** RT Deutsch content-laundering ecosystem  
**Date:** At least early 2024 to February 2025  
**Targets:** German-speaking audiences and Germany’s media environment  
**Perpetrator:** Networks reposting or republishing RT Deutsch content, including mirror and aggregator sites  
**Motivation:** Sustain and expand RT Deutsch’s audience in Germany despite legal restrictions and sanctions

## Cyberattack Details

- **Nature:** Automated reposting, RSS-driven syndication, mirror domains, and search-result flooding
- **Systems Attacked:** Search and discovery environment, website aggregation infrastructure, mirror-domain hosting, and RT content distribution channels
- **Data Held:** RT Deutsch articles, mirror-site copies, RSS feeds, and republished content on aggregator domains, often with obscured origin labels
- **Availability Impact:** No outage reported; the operation preserved the availability of sanctioned media through alternate infrastructure
- **Data Exfiltration/Alteration:** No confirmed exfiltration; content appears mirrored, syndicated, or laundered rather than stolen according to the alert and archive descriptions
- **Estimated Impact:** Collective monthly traffic for identified domains may reach several million visitors globally, and Alliance4Europe archive material indicates continuing sanctions-evasion reporting around RT Germany and related channels
- **Investigators:** Alliance for Securing Democracy, GMF, Alliance4Europe, and listed authors in the alert
- **Remediation:** Increase transparency for aggregators, coordinate with hosting providers and regulators, investigate mirror-domain ownership, and monitor new RT Germany distribution assets on social platforms

## Disinformation Details

- **Nature:** Content laundering and narrative amplification through mirror and aggregator domains
- **Narratives:** Degradation of Western institutions; Germany stifles dissent through censorship; Germany’s support for Ukraine undermines its own interests; the United States imposes its agenda on Europe
- **Deception:** Labeling RT reposts as ordinary news, obscuring authorship, operating mirror or aggregator domains, and using multiple distribution channels to amplify search visibility
- **Platforms:** VK, Telegram, X, Odyssee, Rumble, websites, and various aggregator sites
- **Reach:** Potentially several million monthly visitors collectively
- **Impact:** Continued exposure of German-speaking audiences to sanctioned Russian state media narratives despite restrictions, with evidence that RT Germany kept probing new platform and domain footholds
- **Disinfo Investigators:** Authors and organizations listed in the alert, supplemented by Alliance4Europe sanctions-monitoring reporting
- **Remediation:** Labeling requirements, stakeholder information-sharing, detection of content-laundering patterns, and enforcement against newly surfaced RT Germany channels
- **Link to Cyberattack:** The campaign depends on technical distribution infrastructure—RSS, mirrors, search-result flooding, and new social/distribution accounts—to keep influence content accessible and discoverable

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0047, p. 47  
[2](https://alliance4europe.eu/tag/influence-operations): Alliance4Europe, Influence operations archive entry for RT Germany / sanctions-related reporting  
[3](https://alliance4europe.eu/project_category/digital-intelligence): Alliance4Europe, Digital Intelligence archive listing related sanctions and influence reports  

---

## Incident Summary

**Title:** RT Deutsch access through mirror sites ahead of Germany’s 2025 federal election  
**Date:** February 2025  
**Targets:** German audiences, Germany’s 2025 federal election context, and enforcement credibility of EU sanctions  
**Perpetrator:** Pro-Kremlin actors spreading RT Deutsch through mirror domains and subdomains  
**Motivation:** Preserve access to Russian state media, maintain engagement, and exploit enforcement gaps during a politically sensitive period

## Cyberattack Details

- **Nature:** Mirror domains, subdomains, DNS changes, and traffic redirection through major ISPs and search/social discovery pathways
- **Systems Attacked:** Web access pathways, search/discovery systems, hosting and DNS pathways, and the broader sanctions-enforcement environment
- **Data Held:** RT Deutsch content mirrored across 20 domains and 11 subdomains, plus referral and distribution pathways that kept the content discoverable
- **Availability Impact:** No major outage; instead the operation maintained continued availability of sanctioned content via replacement domains and subdomains
- **Data Exfiltration/Alteration:** No confirmed exfiltration in the alert; the technical mechanism is duplication and rerouting rather than theft
- **Estimated Impact:** Mirror sites available via major German ISPs averaged 45,317 unique organic visitors in December 2024, with top sites ranging from 102,100 to 213,900 visitors; archive material suggests RT Germany also sought fresh footholds on social platforms during the same period
- **Investigators:** Institute for Strategic Dialogue contributors named in the alert, with related monitoring by Alliance4Europe
- **Remediation:** Monitoring and sanctioning mirror sites, restricting monetization and redirecting traffic, ISP and search engine coordination, and stronger enforcement by social platforms

## Disinformation Details

- **Nature:** Repackaged sanctioned media access that preserves distribution of pro-Kremlin narratives
- **Narratives:** Criticism of European foreign policy; degradation of the West; promotion of alternate geopolitical alignment; domestic grievance narratives about support for Ukraine and EVs
- **Deception:** Mirror sites and alternative domains replicating RT content under different names and pathways, combined with sanctions-evasion behavior that obscures continuity with the banned outlet
- **Platforms:** Websites and related discovery channels
- **Reach:** Measurable organic traffic through major German ISPs and continued user engagement that sometimes exceeds pre-sanctions retention levels
- **Impact:** Continued accessibility of Russian state media despite sanctions and possible influence on election-period discourse
- **Disinfo Investigators:** ISD contributors listed in the alert, supplemented by Alliance4Europe tracking of RT Germany sanctions evasion
- **Remediation:** Regulatory tracking, sanctions, common ISP blocklists, exclusion from search/social results, and faster disruption of replacement domains
- **Link to Cyberattack:** The influence effort relies on domain infrastructure, DNS and redirect workarounds, and search/discovery manipulation to keep sanctioned propaganda available

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0048, pp. 48-49  
[2](https://alliance4europe.eu/tag/influence-operations): Alliance4Europe, archive entry showing continued RT Germany sanctions-evasion activity  
[3](https://alliance4europe.eu/project_category/digital-intelligence): Alliance4Europe, Digital Intelligence archive for related sanctions and election-risk reporting  

---

## Incident Summary

**Title:** Overload network impersonates German journalists and organizations  
**Date:** From approximately February 18, 2025  
**Targets:** German election discourse, German voters, journalists, institutions, and fact-checkers  
**Perpetrator:** Accounts tied to the Overload network  
**Motivation:** Support specific narratives affecting the German election, overwhelm observers, and encourage political choices favorable to AfD and anti-immigration themes

## Cyberattack Details

- **Nature:** Manipulated videos, voice-over spoofing, multi-platform impersonation, and automated forwarding/reposting cascades
- **Systems Attacked:** X and Bluesky information ecosystems; reputational trust in journalists and institutions
- **Data Held:** Manipulated videos of real people and institutions, multilingual posts, and bot-cascade forwarding patterns
- **Availability Impact:** No outage reported
- **Data Exfiltration/Alteration:** No confirmed exfiltration; operation altered media artifacts to create deceptive content
- **Estimated Impact:** Minimal reported reach at the time, with posts averaging around 200 likes and shares
- **Investigators:** Alliance4Europe and ISD contributors listed in the alert
- **Remediation:** Archive accounts and content, refine account-surfacing techniques, and flag surfaced accounts to platforms for removal

## Disinformation Details

- **Nature:** Coordinated impersonation campaign using cheapfakes, voice manipulation, and institution spoofing
- **Narratives:** German state institutions cannot serve citizens; radical Islam is overwhelming the West; German authorities cannot protect citizens from terrorist attacks; only AfD can save Germany; discouraging election participation due to security fears
- **Deception:** Impersonated journalists and institutions, AI-generated or edited audio/video, and bot amplification through automated forwarding
- **Platforms:** X and Bluesky
- **Reach:** Limited at the time of review, with low engagement but ongoing activity
- **Impact:** Adds noise to the election information space and increases burdens on fact-checkers and observers
- **Disinfo Investigators:** Alliance4Europe and ISD contributors
- **Remediation:** Archiving, monitoring, and platform reporting
- **Link to Cyberattack:** The operation’s influence effects are built on technical media manipulation, impersonation, and automated reposting rather than simple organic posting

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0049, pp. 49-50  

---

## Incident Summary

**Title:** R-FBI article claiming German Greens will commit election fraud  
**Date:** February 21 to February 23, 2025  
**Targets:** German election discourse, the Green party, and trust in election results  
**Perpetrator:** Russian state-aligned Foundation to Battle Injustice (R-FBI) and amplifying pro-Russian influencers  
**Motivation:** Smear the Greens, discredit the election result, and spread election-fraud narratives

## Cyberattack Details

- **Nature:** Fabricated NGO persona, localized article and video production, and coordinated cross-platform amplification
- **Systems Attacked:** Facebook, X, Telegram, and websites carrying republished or scripted content
- **Data Held:** German-language article and video, screenshots, links, and amplification posts
- **Availability Impact:** No outage reported
- **Data Exfiltration/Alteration:** No confirmed exfiltration in the alert
- **Estimated Impact:** 47,600 views and 1,174 interactions; impact assessed as limited and mostly within pro-Russian spaces
- **Investigators:** CeMAS, Alliance4Europe, and independent contributors listed in the alert
- **Remediation:** Cases flagged to German government agencies and social media platforms; recommendation that the EU enact sanctions against R-FBI

## Disinformation Details

- **Nature:** Fabricated election-fraud claim localized for the German context and spread by influencers
- **Narratives:** The Greens will commit election fraud; election workers will be bribed; postal voting is being manipulated; disinformation campaigns are exposing fraud
- **Deception:** Fabricated NGO persona, scripted human rights framing, localized adaptation, and influencer baiting
- **Platforms:** Facebook, X, and Telegram
- **Reach:** 47,600 views and 1,174 interactions
- **Impact:** Limited measured reach but direct attack on trust in election legitimacy
- **Disinfo Investigators:** CeMAS, Alliance4Europe, and named contributors in the alert
- **Remediation:** Reporting to government agencies and platforms; sanctions recommendation
- **Link to Cyberattack:** The operation combines fabricated organizational identity, localized digital content production, and coordinated cross-platform delivery to weaponize election-fraud narratives

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0051, pp. 51-52  

---

## Incident Summary

**Title:** Russian state media promotes WABEO’s parallel vote tabulation  
**Date:** Lead-up to the German election, February 2025  
**Targets:** German election procedures, public trust in official vote certification, and conspiracy-prone audiences  
**Perpetrator:** WABEO campaign amplified by Russian state media and conspiracy-focused Telegram channels  
**Motivation:** Challenge confidence in official election results and legitimize an unofficial parallel vote-counting initiative

## Cyberattack Details

- **Nature:** App-based private election monitoring initiative amplified through online channels and Russian media ecosystems
- **Systems Attacked:** Election information environment and an unofficial app-based digital vote-reporting mechanism presented as court-proof observation
- **Data Held:** Volunteer-reported vote tallies and observations collected through a proprietary application used by private participants
- **Availability Impact:** No outage reported
- **Data Exfiltration/Alteration:** No public evidence of exfiltration found in this pass, but the integrity, chain of custody, and verification model for privately submitted data remain unclear
- **Estimated Impact:** More than 60,000 Telegram views on promotion of the initiative; WABEO’s own site presents the model as nationwide and court-proof, which increases its potential to influence perceptions of official results
- **Investigators:** Alliance4Europe according to the alert
- **Remediation:** Educate the public on differences between official and private monitoring; investigate WABEO’s funding, methodology, and technical integrity; encourage labeling and disclaimers on hosting platforms

## Disinformation Details

- **Nature:** Election-conspiracy adjacent narrative amplification using state-media legitimization and Telegram promotion
- **Narratives:** Potential electoral irregularities undermine trust in official voting procedures; unofficial observers can produce legally binding or court-proof findings; doubts about Germany’s democratic institutions
- **Deception:** Russian state media amplification lends legitimacy; promotional framing blurs the distinction between official and private election oversight; the website’s “court-proof” framing may overstate the authority of private tabulation outputs
- **Platforms:** Telegram and websites
- **Reach:** More than 60,000 views on Telegram according to the alert
- **Impact:** Could introduce confusion or disputes around official results and increase distrust in democratic procedures, especially if unofficial app-based tallies are framed as superior to official mechanisms
- **Disinfo Investigators:** Alliance4Europe
- **Remediation:** Public education, funding and technical-integrity investigation, stronger transparency rules, and scrutiny of how unofficial data claims are communicated
- **Link to Cyberattack:** The digital application and online dissemination infrastructure are central to turning an unofficial monitoring initiative into an influence vector against trust in election administration

## References

[1](Alerts.pdf): Alerts.pdf, Incident Alert 0052, pp. 52-53  
[2](https://wabeo.org/en/home): WABEO official site, describing nationwide court-proof election observation and app-based volunteer reporting  


