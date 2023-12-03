from django.contrib.auth.models import Permission
from django.db import models


# Create your models here.

class QualityTemplates(models.Model):

    #options for source_entity
    SOURCE_ENTITY_L = (
        ('Import', 'Import'),
        ('Local', 'Local'),
    )

    CATEGORY_L = (
        ('RAWMAT', 'RAWMAT'),
        ('FG', 'FG'),
        ('S-FG', 'S-FG'),
    )

    PRODUCT_CATEGORY_L = (
        ('FABRICS', 'FABRICS'),
        ('PACKAGING ACC', 'PACKAGING ACC'),
        ('INTERIOR', 'INTERIOR'),
        ('BEADS', 'BEADS'),
        ('FIBRE', 'FIBRE'),
        ('H&L', 'H&L'),
    )

    Name = models.CharField(max_length=100, unique=True)
    Description = models.CharField(max_length=100, unique=False)
    CreateDate = models.DateField(null=True, blank=True)
    source_entity = models.CharField(max_length=100, choices=SOURCE_ENTITY_L)
    category = models.CharField(max_length=100, choices=CATEGORY_L)
    product_category = models.CharField(max_length=100, choices=PRODUCT_CATEGORY_L)

    
    class Meta:
        unique_together = ('Name', 'Description', 'source_entity', 'category', 'product_category')

    def __str__(self):
        return self.Name
    
class QualityTemplateItems(models.Model):

    #options for results
    RESULTS_L = (
        ('PASS', 'PASS'),
        ('FAIL', 'FAIL'),
    )

    template_name = models.ForeignKey(QualityTemplates, on_delete=models.CASCADE)
    Test_Property = models.CharField(max_length=100, unique=False)
    Test_Standard = models.CharField(max_length=100, unique=False)
    Standard_Quality_Information = models.CharField(max_length=100, unique=False)
    Test_Requirement = models.CharField(max_length=100, unique=False)
    Requirement_Lower_Range = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Requirement_Upper_Range = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Testing_Line = models.CharField(max_length=100, unique=False)
    Initial_Values = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Line_Result_Value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Result = models.CharField(max_length=100, choices=RESULTS_L)
    Comments = models.CharField(max_length=100, unique=False)
    Test_By = models.CharField(max_length=100, unique=False)
    Date_Of_Test = models.DateField(null=True, blank=True)
    Attachments = models.FileField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.template_name


class QualitySamples(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    template_name = models.CharField(max_length=100, unique=True)
    Description = models.CharField(max_length=100, unique=False)
    CreateDate = models.DateField(null=True, blank=True)
    request_date = models.DateField(null=True, blank=True)
    requestor = models.CharField(max_length=100, unique=False)
    purpose = models.CharField(max_length=100, unique=False)
    pr_no = models.CharField(max_length=100, unique=False)

    class Meta:
        unique_together = ('Name', 'template_name', 'Description', 'request_date', 'requestor', 'purpose', 'pr_no')

class QualitySchedules(models.Model):
      QualitySamples = models.CharField(max_length=100, unique=False)
      Test_Serial_No = models.CharField(max_length=100, unique=False)
      Requestor = models.CharField(max_length=100, unique=False)    
      Department = models.CharField(max_length=100, unique=False)
      Purpose_of_testing = models.CharField(max_length=100, unique=False)
      Brand = models.CharField(max_length=100, unique=False)
      Category = models.CharField(max_length=100, unique=False)
      Product_Category = models.CharField(max_length=100, unique=False)
      Product_Sub_Category = models.CharField(max_length=100, unique=False)
      Collection = models.CharField(max_length=100, unique=False)
      Description_1 = models.CharField(max_length=100, unique=False)
      Description_2 = models.CharField(max_length=100, unique=False)
      SKU = models.CharField(max_length=100, unique=False)
      Source_entity = models.CharField(max_length=100, unique=False)
      Vendor_Name = models.CharField(max_length=100, unique=False)
      Vendor_Code = models.CharField(max_length=100, unique=False)
      Quantity = models.CharField(max_length=100, unique=False)
      RFI_No_RFQ_No_PO_No = models.CharField(max_length=100, unique=False)
      Item_No = models.CharField(max_length=100, unique=False)
      Barcode = models.CharField(max_length=100, unique=False)
      Delivery_Location_Code = models.CharField(max_length=100, unique=False)
      Launch_week = models.CharField(max_length=100, unique=False)
      Launch_month = models.CharField(max_length=100, unique=False)
      Target_Shipment_Date = models.DateField(null=True, blank=True)
      Date_Parcel_Send = models.DateField(null=True, blank=True)
      Courier_Company_Other = models.CharField(max_length=100, unique=False)
      Tracking_Number = models.CharField(max_length=100, unique=False)
      Date_Parcel_Arrive_EA2 = models.DateField(null=True, blank=True)
      Sample_Receive_Date_by_Lab = models.DateField(null=True, blank=True)
      Estimated_Result_Date = models.DateField(null=True, blank=True)
      Estimated_Result_Date_Rev_1 = models.DateField(null=True, blank=True)
      Reason_to_Reshedule_Rev_1 = models.CharField(max_length=100, unique=False)
      Estimated_Result_Date_Rev_2 = models.DateField(null=True, blank=True)
      Reason_to_Reshedule_Rev_2 = models.CharField(max_length=100, unique=False)
      Date_Receive_Complete_Document = models.DateField(null=True, blank=True)
      Date_Start_Test = models.DateField(null=True, blank=True)
      Actual_result_released_date = models.DateField(null=True, blank=True)
      Fabric_Type_M_C_P = models.CharField(max_length=100, unique=False)
      Special_request = models.CharField(max_length=100, unique=False)
      Posting_Date = models.DateField(null=True, blank=True)
      Remarks = models.CharField(max_length=100, unique=False)

        #options for status
      STATUS_L = (
            ('PASS', 'PASS'),
            ('FAIL', 'FAIL'),
            ('In Progress', 'In Progress'),
        )

      Overall_status = models.CharField(max_length=100, unique=False)
      QM_Final_Disposition = models.CharField(max_length=100, unique=False)
      Requestor_Disposition = models.CharField(max_length=100, unique=False)

      #options for assign to
      Assign_To = (
            ('Melvin', 'Melvin'),
            ('Sam', 'Sam'),
            ('Lai Yen', 'Lai Yen'),
            ('Qin', 'Qin'),
        )

      Assign_To = models.CharField(max_length=100, choices=Assign_To)
      
      def __str__(self):
        return self.Test_Serial_No