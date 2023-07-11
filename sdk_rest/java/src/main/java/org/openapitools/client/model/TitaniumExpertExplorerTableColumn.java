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
 * TitaniumExpertExplorerTableColumn
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-07-11T12:02:45.739107Z[UTC]")
public class TitaniumExpertExplorerTableColumn {
  public static final String SERIALIZED_NAME_ABS_DIFF_FROM_EXPERT_COHORT_MEAN = "absDiffFromExpertCohortMean";
  @SerializedName(SERIALIZED_NAME_ABS_DIFF_FROM_EXPERT_COHORT_MEAN)
  private Object absDiffFromExpertCohortMean;

  public static final String SERIALIZED_NAME_CON_PRICE_ABS_DIFF_FROM_LATEST_TRADE = "conPriceAbsDiffFromLatestTrade";
  @SerializedName(SERIALIZED_NAME_CON_PRICE_ABS_DIFF_FROM_LATEST_TRADE)
  private Object conPriceAbsDiffFromLatestTrade;

  public static final String SERIALIZED_NAME_MAX = "max";
  @SerializedName(SERIALIZED_NAME_MAX)
  private Object max;

  public static final String SERIALIZED_NAME_MEAN = "mean";
  @SerializedName(SERIALIZED_NAME_MEAN)
  private Object mean;

  public static final String SERIALIZED_NAME_MIN = "min";
  @SerializedName(SERIALIZED_NAME_MIN)
  private Object min;

  public static final String SERIALIZED_NAME_PARTICIPANT_INSTRUMENTS_COUNT = "participantInstrumentsCount";
  @SerializedName(SERIALIZED_NAME_PARTICIPANT_INSTRUMENTS_COUNT)
  private String participantInstrumentsCount;

  public static final String SERIALIZED_NAME_STD_DEV = "stdDev";
  @SerializedName(SERIALIZED_NAME_STD_DEV)
  private Object stdDev;

  public static final String SERIALIZED_NAME_SUB_PRICE_DIFF = "subPriceDiff";
  @SerializedName(SERIALIZED_NAME_SUB_PRICE_DIFF)
  private Object subPriceDiff;

  public TitaniumExpertExplorerTableColumn() { 
  }

  public TitaniumExpertExplorerTableColumn absDiffFromExpertCohortMean(Object absDiffFromExpertCohortMean) {
    
    this.absDiffFromExpertCohortMean = absDiffFromExpertCohortMean;
    return this;
  }

   /**
   * Get absDiffFromExpertCohortMean
   * @return absDiffFromExpertCohortMean
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getAbsDiffFromExpertCohortMean() {
    return absDiffFromExpertCohortMean;
  }


  public void setAbsDiffFromExpertCohortMean(Object absDiffFromExpertCohortMean) {
    this.absDiffFromExpertCohortMean = absDiffFromExpertCohortMean;
  }


  public TitaniumExpertExplorerTableColumn conPriceAbsDiffFromLatestTrade(Object conPriceAbsDiffFromLatestTrade) {
    
    this.conPriceAbsDiffFromLatestTrade = conPriceAbsDiffFromLatestTrade;
    return this;
  }

   /**
   * Get conPriceAbsDiffFromLatestTrade
   * @return conPriceAbsDiffFromLatestTrade
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getConPriceAbsDiffFromLatestTrade() {
    return conPriceAbsDiffFromLatestTrade;
  }


  public void setConPriceAbsDiffFromLatestTrade(Object conPriceAbsDiffFromLatestTrade) {
    this.conPriceAbsDiffFromLatestTrade = conPriceAbsDiffFromLatestTrade;
  }


  public TitaniumExpertExplorerTableColumn max(Object max) {
    
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


  public TitaniumExpertExplorerTableColumn mean(Object mean) {
    
    this.mean = mean;
    return this;
  }

   /**
   * Get mean
   * @return mean
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getMean() {
    return mean;
  }


  public void setMean(Object mean) {
    this.mean = mean;
  }


  public TitaniumExpertExplorerTableColumn min(Object min) {
    
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


  public TitaniumExpertExplorerTableColumn participantInstrumentsCount(String participantInstrumentsCount) {
    
    this.participantInstrumentsCount = participantInstrumentsCount;
    return this;
  }

   /**
   * Get participantInstrumentsCount
   * @return participantInstrumentsCount
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getParticipantInstrumentsCount() {
    return participantInstrumentsCount;
  }


  public void setParticipantInstrumentsCount(String participantInstrumentsCount) {
    this.participantInstrumentsCount = participantInstrumentsCount;
  }


  public TitaniumExpertExplorerTableColumn stdDev(Object stdDev) {
    
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


  public TitaniumExpertExplorerTableColumn subPriceDiff(Object subPriceDiff) {
    
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumExpertExplorerTableColumn titaniumExpertExplorerTableColumn = (TitaniumExpertExplorerTableColumn) o;
    return Objects.equals(this.absDiffFromExpertCohortMean, titaniumExpertExplorerTableColumn.absDiffFromExpertCohortMean) &&
        Objects.equals(this.conPriceAbsDiffFromLatestTrade, titaniumExpertExplorerTableColumn.conPriceAbsDiffFromLatestTrade) &&
        Objects.equals(this.max, titaniumExpertExplorerTableColumn.max) &&
        Objects.equals(this.mean, titaniumExpertExplorerTableColumn.mean) &&
        Objects.equals(this.min, titaniumExpertExplorerTableColumn.min) &&
        Objects.equals(this.participantInstrumentsCount, titaniumExpertExplorerTableColumn.participantInstrumentsCount) &&
        Objects.equals(this.stdDev, titaniumExpertExplorerTableColumn.stdDev) &&
        Objects.equals(this.subPriceDiff, titaniumExpertExplorerTableColumn.subPriceDiff);
  }

  @Override
  public int hashCode() {
    return Objects.hash(absDiffFromExpertCohortMean, conPriceAbsDiffFromLatestTrade, max, mean, min, participantInstrumentsCount, stdDev, subPriceDiff);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumExpertExplorerTableColumn {\n");
    sb.append("    absDiffFromExpertCohortMean: ").append(toIndentedString(absDiffFromExpertCohortMean)).append("\n");
    sb.append("    conPriceAbsDiffFromLatestTrade: ").append(toIndentedString(conPriceAbsDiffFromLatestTrade)).append("\n");
    sb.append("    max: ").append(toIndentedString(max)).append("\n");
    sb.append("    mean: ").append(toIndentedString(mean)).append("\n");
    sb.append("    min: ").append(toIndentedString(min)).append("\n");
    sb.append("    participantInstrumentsCount: ").append(toIndentedString(participantInstrumentsCount)).append("\n");
    sb.append("    stdDev: ").append(toIndentedString(stdDev)).append("\n");
    sb.append("    subPriceDiff: ").append(toIndentedString(subPriceDiff)).append("\n");
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
    openapiFields.add("absDiffFromExpertCohortMean");
    openapiFields.add("conPriceAbsDiffFromLatestTrade");
    openapiFields.add("max");
    openapiFields.add("mean");
    openapiFields.add("min");
    openapiFields.add("participantInstrumentsCount");
    openapiFields.add("stdDev");
    openapiFields.add("subPriceDiff");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumExpertExplorerTableColumn
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumExpertExplorerTableColumn.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumExpertExplorerTableColumn is not found in the empty JSON string", TitaniumExpertExplorerTableColumn.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumExpertExplorerTableColumn.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumExpertExplorerTableColumn` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("participantInstrumentsCount") != null && !jsonObj.get("participantInstrumentsCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `participantInstrumentsCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("participantInstrumentsCount").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumExpertExplorerTableColumn.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumExpertExplorerTableColumn' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumExpertExplorerTableColumn> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumExpertExplorerTableColumn.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumExpertExplorerTableColumn>() {
           @Override
           public void write(JsonWriter out, TitaniumExpertExplorerTableColumn value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumExpertExplorerTableColumn read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumExpertExplorerTableColumn given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumExpertExplorerTableColumn
  * @throws IOException if the JSON string is invalid with respect to TitaniumExpertExplorerTableColumn
  */
  public static TitaniumExpertExplorerTableColumn fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumExpertExplorerTableColumn.class);
  }

 /**
  * Convert an instance of TitaniumExpertExplorerTableColumn to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

