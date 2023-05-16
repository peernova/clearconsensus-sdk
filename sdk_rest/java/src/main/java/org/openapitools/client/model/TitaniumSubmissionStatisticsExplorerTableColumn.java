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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-05-16T13:23:08.957131Z[UTC]")
public class TitaniumSubmissionStatisticsExplorerTableColumn {
  public static final String SERIALIZED_NAME_ABS_DIFF_FROM_STATISTICAL_MEAN = "absDiffFromStatisticalMean";
  @SerializedName(SERIALIZED_NAME_ABS_DIFF_FROM_STATISTICAL_MEAN)
  private Object absDiffFromStatisticalMean;

  public static final String SERIALIZED_NAME_LOWER_BOUNDARY = "lowerBoundary";
  @SerializedName(SERIALIZED_NAME_LOWER_BOUNDARY)
  private Object lowerBoundary;

  public static final String SERIALIZED_NAME_MAX = "max";
  @SerializedName(SERIALIZED_NAME_MAX)
  private Object max;

  public static final String SERIALIZED_NAME_MIN = "min";
  @SerializedName(SERIALIZED_NAME_MIN)
  private Object min;

  public static final String SERIALIZED_NAME_STATISTICAL_MEAN = "statisticalMean";
  @SerializedName(SERIALIZED_NAME_STATISTICAL_MEAN)
  private Object statisticalMean;

  public static final String SERIALIZED_NAME_STD_DEV = "stdDev";
  @SerializedName(SERIALIZED_NAME_STD_DEV)
  private Object stdDev;

  public static final String SERIALIZED_NAME_SUB_PRICE_DIFF = "subPriceDiff";
  @SerializedName(SERIALIZED_NAME_SUB_PRICE_DIFF)
  private Object subPriceDiff;

  public static final String SERIALIZED_NAME_SUB_VALID_POINTS_COUNT = "subValidPointsCount";
  @SerializedName(SERIALIZED_NAME_SUB_VALID_POINTS_COUNT)
  private String subValidPointsCount;

  public static final String SERIALIZED_NAME_UPPER_BOUNDARY = "upperBoundary";
  @SerializedName(SERIALIZED_NAME_UPPER_BOUNDARY)
  private Object upperBoundary;

  public TitaniumSubmissionStatisticsExplorerTableColumn() { 
  }

  public TitaniumSubmissionStatisticsExplorerTableColumn absDiffFromStatisticalMean(Object absDiffFromStatisticalMean) {
    
    this.absDiffFromStatisticalMean = absDiffFromStatisticalMean;
    return this;
  }

   /**
   * Get absDiffFromStatisticalMean
   * @return absDiffFromStatisticalMean
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getAbsDiffFromStatisticalMean() {
    return absDiffFromStatisticalMean;
  }


  public void setAbsDiffFromStatisticalMean(Object absDiffFromStatisticalMean) {
    this.absDiffFromStatisticalMean = absDiffFromStatisticalMean;
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


  public TitaniumSubmissionStatisticsExplorerTableColumn max(Object max) {
    
    this.max = max;
    return this;
  }

   /**
   * Get max
   * @return max
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getMax() {
    return max;
  }


  public void setMax(Object max) {
    this.max = max;
  }


  public TitaniumSubmissionStatisticsExplorerTableColumn min(Object min) {
    
    this.min = min;
    return this;
  }

   /**
   * Get min
   * @return min
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getMin() {
    return min;
  }


  public void setMin(Object min) {
    this.min = min;
  }


  public TitaniumSubmissionStatisticsExplorerTableColumn statisticalMean(Object statisticalMean) {
    
    this.statisticalMean = statisticalMean;
    return this;
  }

   /**
   * Get statisticalMean
   * @return statisticalMean
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getStatisticalMean() {
    return statisticalMean;
  }


  public void setStatisticalMean(Object statisticalMean) {
    this.statisticalMean = statisticalMean;
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


  public TitaniumSubmissionStatisticsExplorerTableColumn subValidPointsCount(String subValidPointsCount) {
    
    this.subValidPointsCount = subValidPointsCount;
    return this;
  }

   /**
   * Get subValidPointsCount
   * @return subValidPointsCount
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getSubValidPointsCount() {
    return subValidPointsCount;
  }


  public void setSubValidPointsCount(String subValidPointsCount) {
    this.subValidPointsCount = subValidPointsCount;
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
    return Objects.equals(this.absDiffFromStatisticalMean, titaniumSubmissionStatisticsExplorerTableColumn.absDiffFromStatisticalMean) &&
        Objects.equals(this.lowerBoundary, titaniumSubmissionStatisticsExplorerTableColumn.lowerBoundary) &&
        Objects.equals(this.max, titaniumSubmissionStatisticsExplorerTableColumn.max) &&
        Objects.equals(this.min, titaniumSubmissionStatisticsExplorerTableColumn.min) &&
        Objects.equals(this.statisticalMean, titaniumSubmissionStatisticsExplorerTableColumn.statisticalMean) &&
        Objects.equals(this.stdDev, titaniumSubmissionStatisticsExplorerTableColumn.stdDev) &&
        Objects.equals(this.subPriceDiff, titaniumSubmissionStatisticsExplorerTableColumn.subPriceDiff) &&
        Objects.equals(this.subValidPointsCount, titaniumSubmissionStatisticsExplorerTableColumn.subValidPointsCount) &&
        Objects.equals(this.upperBoundary, titaniumSubmissionStatisticsExplorerTableColumn.upperBoundary);
  }

  @Override
  public int hashCode() {
    return Objects.hash(absDiffFromStatisticalMean, lowerBoundary, max, min, statisticalMean, stdDev, subPriceDiff, subValidPointsCount, upperBoundary);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumSubmissionStatisticsExplorerTableColumn {\n");
    sb.append("    absDiffFromStatisticalMean: ").append(toIndentedString(absDiffFromStatisticalMean)).append("\n");
    sb.append("    lowerBoundary: ").append(toIndentedString(lowerBoundary)).append("\n");
    sb.append("    max: ").append(toIndentedString(max)).append("\n");
    sb.append("    min: ").append(toIndentedString(min)).append("\n");
    sb.append("    statisticalMean: ").append(toIndentedString(statisticalMean)).append("\n");
    sb.append("    stdDev: ").append(toIndentedString(stdDev)).append("\n");
    sb.append("    subPriceDiff: ").append(toIndentedString(subPriceDiff)).append("\n");
    sb.append("    subValidPointsCount: ").append(toIndentedString(subValidPointsCount)).append("\n");
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
    openapiFields.add("absDiffFromStatisticalMean");
    openapiFields.add("lowerBoundary");
    openapiFields.add("max");
    openapiFields.add("min");
    openapiFields.add("statisticalMean");
    openapiFields.add("stdDev");
    openapiFields.add("subPriceDiff");
    openapiFields.add("subValidPointsCount");
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
      if (jsonObj.get("subValidPointsCount") != null && !jsonObj.get("subValidPointsCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subValidPointsCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subValidPointsCount").toString()));
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

