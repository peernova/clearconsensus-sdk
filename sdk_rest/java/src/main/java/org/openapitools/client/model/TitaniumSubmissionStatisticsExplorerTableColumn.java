/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumSubmissionStatisticsExplorerTableColumn
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-08-24T07:13:26.014483Z[UTC]")
public class TitaniumSubmissionStatisticsExplorerTableColumn {
  public static final String SERIALIZED_NAME_ABS_DIFF_FROM_SUB_EVIDENCE = "absDiffFromSubEvidence";
  @SerializedName(SERIALIZED_NAME_ABS_DIFF_FROM_SUB_EVIDENCE)
  private Object absDiffFromSubEvidence;

  public static final String SERIALIZED_NAME_LOWER_BOUNDARY = "lowerBoundary";
  @SerializedName(SERIALIZED_NAME_LOWER_BOUNDARY)
  private Object lowerBoundary;

  public static final String SERIALIZED_NAME_NUMBER_OF_PART_IN_BOUNDARIES = "numberOfPartInBoundaries";
  @SerializedName(SERIALIZED_NAME_NUMBER_OF_PART_IN_BOUNDARIES)
  private Object numberOfPartInBoundaries;

  public static final String SERIALIZED_NAME_STAT_MEAN_ABS_DIFF_FROM_LATEST_TRADE = "statMeanAbsDiffFromLatestTrade";
  @SerializedName(SERIALIZED_NAME_STAT_MEAN_ABS_DIFF_FROM_LATEST_TRADE)
  private Object statMeanAbsDiffFromLatestTrade;

  public static final String SERIALIZED_NAME_STD_DEV = "stdDev";
  @SerializedName(SERIALIZED_NAME_STD_DEV)
  private Object stdDev;

  public static final String SERIALIZED_NAME_SUB_PRICE_DIFF = "subPriceDiff";
  @SerializedName(SERIALIZED_NAME_SUB_PRICE_DIFF)
  private Object subPriceDiff;

  public static final String SERIALIZED_NAME_SUBMISSION_EVIDENCE = "submissionEvidence";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_EVIDENCE)
  private Object submissionEvidence;

  public static final String SERIALIZED_NAME_SUBMISSION_MAX = "submissionMax";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_MAX)
  private Object submissionMax;

  public static final String SERIALIZED_NAME_SUBMISSION_MIN = "submissionMin";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_MIN)
  private Object submissionMin;

  public static final String SERIALIZED_NAME_UPPER_BOUNDARY = "upperBoundary";
  @SerializedName(SERIALIZED_NAME_UPPER_BOUNDARY)
  private Object upperBoundary;

  public TitaniumSubmissionStatisticsExplorerTableColumn() { 
  }

  public TitaniumSubmissionStatisticsExplorerTableColumn absDiffFromSubEvidence(Object absDiffFromSubEvidence) {
    
    this.absDiffFromSubEvidence = absDiffFromSubEvidence;
    return this;
  }

   /**
   * Get absDiffFromSubEvidence
   * @return absDiffFromSubEvidence
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getAbsDiffFromSubEvidence() {
    return absDiffFromSubEvidence;
  }


  public void setAbsDiffFromSubEvidence(Object absDiffFromSubEvidence) {
    this.absDiffFromSubEvidence = absDiffFromSubEvidence;
  }


  public TitaniumSubmissionStatisticsExplorerTableColumn lowerBoundary(Object lowerBoundary) {
    
    this.lowerBoundary = lowerBoundary;
    return this;
  }

   /**
   * Get lowerBoundary
   * @return lowerBoundary
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getLowerBoundary() {
    return lowerBoundary;
  }


  public void setLowerBoundary(Object lowerBoundary) {
    this.lowerBoundary = lowerBoundary;
  }


  public TitaniumSubmissionStatisticsExplorerTableColumn numberOfPartInBoundaries(Object numberOfPartInBoundaries) {
    
    this.numberOfPartInBoundaries = numberOfPartInBoundaries;
    return this;
  }

   /**
   * Get numberOfPartInBoundaries
   * @return numberOfPartInBoundaries
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getNumberOfPartInBoundaries() {
    return numberOfPartInBoundaries;
  }


  public void setNumberOfPartInBoundaries(Object numberOfPartInBoundaries) {
    this.numberOfPartInBoundaries = numberOfPartInBoundaries;
  }


  public TitaniumSubmissionStatisticsExplorerTableColumn statMeanAbsDiffFromLatestTrade(Object statMeanAbsDiffFromLatestTrade) {
    
    this.statMeanAbsDiffFromLatestTrade = statMeanAbsDiffFromLatestTrade;
    return this;
  }

   /**
   * Get statMeanAbsDiffFromLatestTrade
   * @return statMeanAbsDiffFromLatestTrade
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getStatMeanAbsDiffFromLatestTrade() {
    return statMeanAbsDiffFromLatestTrade;
  }


  public void setStatMeanAbsDiffFromLatestTrade(Object statMeanAbsDiffFromLatestTrade) {
    this.statMeanAbsDiffFromLatestTrade = statMeanAbsDiffFromLatestTrade;
  }


  public TitaniumSubmissionStatisticsExplorerTableColumn stdDev(Object stdDev) {
    
    this.stdDev = stdDev;
    return this;
  }

   /**
   * Get stdDev
   * @return stdDev
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getStdDev() {
    return stdDev;
  }


  public void setStdDev(Object stdDev) {
    this.stdDev = stdDev;
  }


  public TitaniumSubmissionStatisticsExplorerTableColumn subPriceDiff(Object subPriceDiff) {
    
    this.subPriceDiff = subPriceDiff;
    return this;
  }

   /**
   * Get subPriceDiff
   * @return subPriceDiff
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getSubPriceDiff() {
    return subPriceDiff;
  }


  public void setSubPriceDiff(Object subPriceDiff) {
    this.subPriceDiff = subPriceDiff;
  }


  public TitaniumSubmissionStatisticsExplorerTableColumn submissionEvidence(Object submissionEvidence) {
    
    this.submissionEvidence = submissionEvidence;
    return this;
  }

   /**
   * Get submissionEvidence
   * @return submissionEvidence
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getSubmissionEvidence() {
    return submissionEvidence;
  }


  public void setSubmissionEvidence(Object submissionEvidence) {
    this.submissionEvidence = submissionEvidence;
  }


  public TitaniumSubmissionStatisticsExplorerTableColumn submissionMax(Object submissionMax) {
    
    this.submissionMax = submissionMax;
    return this;
  }

   /**
   * Get submissionMax
   * @return submissionMax
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getSubmissionMax() {
    return submissionMax;
  }


  public void setSubmissionMax(Object submissionMax) {
    this.submissionMax = submissionMax;
  }


  public TitaniumSubmissionStatisticsExplorerTableColumn submissionMin(Object submissionMin) {
    
    this.submissionMin = submissionMin;
    return this;
  }

   /**
   * Get submissionMin
   * @return submissionMin
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getSubmissionMin() {
    return submissionMin;
  }


  public void setSubmissionMin(Object submissionMin) {
    this.submissionMin = submissionMin;
  }


  public TitaniumSubmissionStatisticsExplorerTableColumn upperBoundary(Object upperBoundary) {
    
    this.upperBoundary = upperBoundary;
    return this;
  }

   /**
   * Get upperBoundary
   * @return upperBoundary
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getUpperBoundary() {
    return upperBoundary;
  }


  public void setUpperBoundary(Object upperBoundary) {
    this.upperBoundary = upperBoundary;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumSubmissionStatisticsExplorerTableColumn titaniumSubmissionStatisticsExplorerTableColumn = (TitaniumSubmissionStatisticsExplorerTableColumn) o;
    return Objects.equals(this.absDiffFromSubEvidence, titaniumSubmissionStatisticsExplorerTableColumn.absDiffFromSubEvidence) &&
        Objects.equals(this.lowerBoundary, titaniumSubmissionStatisticsExplorerTableColumn.lowerBoundary) &&
        Objects.equals(this.numberOfPartInBoundaries, titaniumSubmissionStatisticsExplorerTableColumn.numberOfPartInBoundaries) &&
        Objects.equals(this.statMeanAbsDiffFromLatestTrade, titaniumSubmissionStatisticsExplorerTableColumn.statMeanAbsDiffFromLatestTrade) &&
        Objects.equals(this.stdDev, titaniumSubmissionStatisticsExplorerTableColumn.stdDev) &&
        Objects.equals(this.subPriceDiff, titaniumSubmissionStatisticsExplorerTableColumn.subPriceDiff) &&
        Objects.equals(this.submissionEvidence, titaniumSubmissionStatisticsExplorerTableColumn.submissionEvidence) &&
        Objects.equals(this.submissionMax, titaniumSubmissionStatisticsExplorerTableColumn.submissionMax) &&
        Objects.equals(this.submissionMin, titaniumSubmissionStatisticsExplorerTableColumn.submissionMin) &&
        Objects.equals(this.upperBoundary, titaniumSubmissionStatisticsExplorerTableColumn.upperBoundary);
  }

  @Override
  public int hashCode() {
    return Objects.hash(absDiffFromSubEvidence, lowerBoundary, numberOfPartInBoundaries, statMeanAbsDiffFromLatestTrade, stdDev, subPriceDiff, submissionEvidence, submissionMax, submissionMin, upperBoundary);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumSubmissionStatisticsExplorerTableColumn {\n");
    sb.append("    absDiffFromSubEvidence: ").append(toIndentedString(absDiffFromSubEvidence)).append("\n");
    sb.append("    lowerBoundary: ").append(toIndentedString(lowerBoundary)).append("\n");
    sb.append("    numberOfPartInBoundaries: ").append(toIndentedString(numberOfPartInBoundaries)).append("\n");
    sb.append("    statMeanAbsDiffFromLatestTrade: ").append(toIndentedString(statMeanAbsDiffFromLatestTrade)).append("\n");
    sb.append("    stdDev: ").append(toIndentedString(stdDev)).append("\n");
    sb.append("    subPriceDiff: ").append(toIndentedString(subPriceDiff)).append("\n");
    sb.append("    submissionEvidence: ").append(toIndentedString(submissionEvidence)).append("\n");
    sb.append("    submissionMax: ").append(toIndentedString(submissionMax)).append("\n");
    sb.append("    submissionMin: ").append(toIndentedString(submissionMin)).append("\n");
    sb.append("    upperBoundary: ").append(toIndentedString(upperBoundary)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("absDiffFromSubEvidence");
    openapiFields.add("lowerBoundary");
    openapiFields.add("numberOfPartInBoundaries");
    openapiFields.add("statMeanAbsDiffFromLatestTrade");
    openapiFields.add("stdDev");
    openapiFields.add("subPriceDiff");
    openapiFields.add("submissionEvidence");
    openapiFields.add("submissionMax");
    openapiFields.add("submissionMin");
    openapiFields.add("upperBoundary");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumSubmissionStatisticsExplorerTableColumn
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumSubmissionStatisticsExplorerTableColumn.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumSubmissionStatisticsExplorerTableColumn is not found in the empty JSON string", TitaniumSubmissionStatisticsExplorerTableColumn.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumSubmissionStatisticsExplorerTableColumn.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumSubmissionStatisticsExplorerTableColumn` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumSubmissionStatisticsExplorerTableColumn.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumSubmissionStatisticsExplorerTableColumn' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumSubmissionStatisticsExplorerTableColumn> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumSubmissionStatisticsExplorerTableColumn.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumSubmissionStatisticsExplorerTableColumn>() {
           @Override
           public void write(JsonWriter out, TitaniumSubmissionStatisticsExplorerTableColumn value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumSubmissionStatisticsExplorerTableColumn read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumSubmissionStatisticsExplorerTableColumn given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumSubmissionStatisticsExplorerTableColumn
  * @throws IOException if the JSON string is invalid with respect to TitaniumSubmissionStatisticsExplorerTableColumn
  */
  public static TitaniumSubmissionStatisticsExplorerTableColumn fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumSubmissionStatisticsExplorerTableColumn.class);
  }

 /**
  * Convert an instance of TitaniumSubmissionStatisticsExplorerTableColumn to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

