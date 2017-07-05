# DATA SCRAPPING THE BOSTON CARES CORPORATE SURVEYS
# FOR BOSTON CARES GROUP 1: VISUALIZE BOSTON
# MATTHEW MORGAN

import os
from openpyxl import load_workbook
import csv
#giving the path directory for finding the survey results
directoryPath=r'/Users/mattmorgan/Documents/Spring2017Semester/VisualizationofData/SurveyMonkeySurveys'
os.chdir(directoryPath)
folder_list=os.listdir(directoryPath)
#creating the initial array to store the data
data = [['activity', 'total volunteers','hasVolunteeredCount', 'BostonCaresMemberCount',
         'I feel the information I was given (project description, schedule, directions, etc) prior to the project '
         'adequately prepared me for the day.',
         'I was provided a good introduction by the agency staff about the work they do and the work we were given.',
         'I feel the project was well organized. (e.g. task assignments, adaquate supplies, etc)',
         'I understand how the work I was doing responded to a community need.',
         'I feel that my time was well utilized and my efforts were appreciated.',
         'The work I did was personally satisfying.',
         'My interactions with Boston Cares Project Leaders were positive.',
         'My interactions with the host site staff were positive.',
         'Overall, I feel the volunteer project was worthwhile.',
         'As a result of this experience, I would consider volunteering with this project again.',
         'ExpectationsExceededCount', 'ExpectationsMetCount', 'ExpectationsNotMetCount',
         'FAVORITE:Camaraderie/socialization/teamwork: working with co-workers, meeting new people',
         'FAVORITE:Altruism: Helping a good cause/others, giving back to the community',
         'FAVORITE:Impact: Seeing results, difference made',
         'FAVORITE:Learning something new: Learning about an organization, learning a new skill',
         'FAVORITE:Interaction: Meeting/working with agency staff, meeting/working with agency clients',
         'FAVORITE:Work assigned: Painting, cleaning, gardening, etc.',
         'FAVORITE:Enjoyment: Having fun',
         'FAVORITE:Environment: Being outdoors',
         'Year']]
#intializing the year value
year = 2011
for folders, sub_folders, file in os.walk(directoryPath): #Traversing the sub folders
    year += 1
    for name in file:
        if name.endswith(".xlsx"):
            filename = os.path.join(folders, name)
            wb=load_workbook(filename, data_only=True)
            ws=wb.active
            sheet = wb.get_sheet_by_name('Questions')
            #parsing the excel sheets for the required values.
            sheetData = [sheet['A1'].value,  sheet['D14'].value,  sheet['D12'].value, sheet['D20'].value, sheet['I28'].value,
                         sheet['I29'].value, sheet['I30'].value, sheet['I31'].value, sheet['I32'].value,
                         sheet['I33'].value, sheet['I34'].value, sheet['I35'].value, sheet['I36'].value,
                         sheet['I37'].value, sheet['D44'].value, sheet['D45'].value, sheet['D46'].value,
                         sheet['C53'].value, sheet['C54'].value, sheet['C55'].value, sheet['C56'].value,
                         sheet['C57'].value, sheet['C58'].value, sheet['C59'].value, sheet['C60'].value,
                         year]
            data.append(sheetData)

with open("output.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
