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
import org.openapitools.client.model.TitaniumAvailableTrades;
import org.openapitools.client.model.TitaniumConsensusColumn;
import org.openapitools.client.model.TitaniumEvidentalPricing;
import org.openapitools.client.model.TitaniumSubmissionColumn;
import org.openapitools.client.model.TitaniumSubmissionRangeColumn;
import org.openapitools.client.model.TitaniumSubmissionStatisticsColumn;

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
 * TitaniumComparisonTable
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-09T11:12:58.692846Z[UTC]")
public class TitaniumComparisonTable {
  public static final String SERIALIZED_NAME_CONSENSUS = "consensus";
  @SerializedName(SERIALIZED_NAME_CONSENSUS)
  private TitaniumConsensusColumn consensus;

  public static final String SERIALIZED_NAME_EVIDENTIAL_PRICING = "evidentialPricing";
  @SerializedName(SERIALIZED_NAME_EVIDENTIAL_PRICING)
  private TitaniumEvidentalPricing evidentialPricing;

  public static final String SERIALIZED_NAME_MY_SUBMISSION = "mySubmission";
  @SerializedName(SERIALIZED_NAME_MY_SUBMISSION)
  private TitaniumSubmissionColumn mySubmission;

  public static final String SERIALIZED_NAME_SUBMISSION_RANGE = "submissionRange";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_RANGE)
  private TitaniumSubmissionRangeColumn submissionRange;

  public static final String SERIALIZED_NAME_SUBMISSION_STATISTICAL_BOUNDARIES = "submissionStatisticalBoundaries";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_STATISTICAL_BOUNDARIES)
  private TitaniumSubmissionStatisticsColumn submissionStatisticalBoundaries;

  public static final String SERIALIZED_NAME_TRADE_TIME_SERIES = "tradeTimeSeries";
  @SerializedName(SERIALIZED_NAME_TRADE_TIME_SERIES)
  private TitaniumAvailableTrades tradeTimeSeries;

  public TitaniumComparisonTable() { 
  }

  public TitaniumComparisonTable consensus(TitaniumConsensusColumn consensus) {
    
    this.consensus = consensus;
    return this;
  }

   /**
   * Get consensus
   * @return consensus
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumConsensusColumn getConsensus() {
    return consensus;
  }


  public void setConsensus(TitaniumConsensusColumn consensus) {
    this.consensus = consensus;
  }


  public TitaniumComparisonTable evidentialPricing(TitaniumEvidentalPricing evidentialPricing) {
    
    this.evidentialPricing = evidentialPricing;
    return this;
  }

   /**
   * Get evidentialPricing
   * @return evidentialPricing
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumEvidentalPricing getEvidentialPricing() {
    return evidentialPricing;
  }


  public void setEvidentialPricing(TitaniumEvidentalPricing evidentialPricing) {
    this.evidentialPricing = evidentialPricing;
  }


  public TitaniumComparisonTable mySubmission(TitaniumSubmissionColumn mySubmission) {
    
    this.mySubmission = mySubmission;
    return this;
  }

   /**
   * Get mySubmission
   * @return mySubmission
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumSubmissionColumn getMySubmission() {
    return mySubmission;
  }


  public void setMySubmission(TitaniumSubmissionColumn mySubmission) {
    this.mySubmission = mySubmission;
  }


  public TitaniumComparisonTable submissionRange(TitaniumSubmissionRangeColumn submissionRange) {
    
    this.submissionRange = submissionRange;
    return this;
  }

   /**
   * Get submissionRange
   * @return submissionRange
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumSubmissionRangeColumn getSubmissionRange() {
    return submissionRange;
  }


  public void setSubmissionRange(TitaniumSubmissionRangeColumn submissionRange) {
    this.submissionRange = submissionRange;
  }


  public TitaniumComparisonTable submissionStatisticalBoundaries(TitaniumSubmissionStatisticsColumn submissionStatisticalBoundaries) {
    
    this.submissionStatisticalBoundaries = submissionStatisticalBoundaries;
    return this;
  }

   /**
   * Get submissionStatisticalBoundaries
   * @return submissionStatisticalBoundaries
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumSubmissionStatisticsColumn getSubmissionStatisticalBoundaries() {
    return submissionStatisticalBoundaries;
  }


  public void setSubmissionStatisticalBoundaries(TitaniumSubmissionStatisticsColumn submissionStatisticalBoundaries) {
    this.submissionStatisticalBoundaries = submissionStatisticalBoundaries;
  }


  public TitaniumComparisonTable tradeTimeSeries(TitaniumAvailableTrades tradeTimeSeries) {
    
    this.tradeTimeSeries = tradeTimeSeries;
    return this;
  }

   /**
   * Get tradeTimeSeries
   * @return tradeTimeSeries
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumAvailableTrades getTradeTimeSeries() {
    return tradeTimeSeries;
  }


  public void setTradeTimeSeries(TitaniumAvailableTrades tradeTimeSeries) {
    this.tradeTimeSeries = tradeTimeSeries;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumComparisonTable titaniumComparisonTable = (TitaniumComparisonTable) o;
    return Objects.equals(this.consensus, titaniumComparisonTable.consensus) &&
        Objects.equals(this.evidentialPricing, titaniumComparisonTable.evidentialPricing) &&
        Objects.equals(this.mySubmission, titaniumComparisonTable.mySubmission) &&
        Objects.equals(this.submissionRange, titaniumComparisonTable.submissionRange) &&
        Objects.equals(this.submissionStatisticalBoundaries, titaniumComparisonTable.submissionStatisticalBoundaries) &&
        Objects.equals(this.tradeTimeSeries, titaniumComparisonTable.tradeTimeSeries);
  }

  @Override
  public int hashCode() {
    return Objects.hash(consensus, evidentialPricing, mySubmission, submissionRange, submissionStatisticalBoundaries, tradeTimeSeries);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumComparisonTable {\n");
    sb.append("    consensus: ").append(toIndentedString(consensus)).append("\n");
    sb.append("    evidentialPricing: ").append(toIndentedString(evidentialPricing)).append("\n");
    sb.append("    mySubmission: ").append(toIndentedString(mySubmission)).append("\n");
    sb.append("    submissionRange: ").append(toIndentedString(submissionRange)).append("\n");
    sb.append("    submissionStatisticalBoundaries: ").append(toIndentedString(submissionStatisticalBoundaries)).append("\n");
    sb.append("    tradeTimeSeries: ").append(toIndentedString(tradeTimeSeries)).append("\n");
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
    openapiFields.add("consensus");
    openapiFields.add("evidentialPricing");
    openapiFields.add("mySubmission");
    openapiFields.add("submissionRange");
    openapiFields.add("submissionStatisticalBoundaries");
    openapiFields.add("tradeTimeSeries");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumComparisonTable
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumComparisonTable.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumComparisonTable is not found in the empty JSON string", TitaniumComparisonTable.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumComparisonTable.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumComparisonTable` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      // validate the optional field `consensus`
      if (jsonObj.getAsJsonObject("consensus") != null) {
        TitaniumConsensusColumn.validateJsonObject(jsonObj.getAsJsonObject("consensus"));
      }
      // validate the optional field `evidentialPricing`
      if (jsonObj.getAsJsonObject("evidentialPricing") != null) {
        TitaniumEvidentalPricing.validateJsonObject(jsonObj.getAsJsonObject("evidentialPricing"));
      }
      // validate the optional field `mySubmission`
      if (jsonObj.getAsJsonObject("mySubmission") != null) {
        TitaniumSubmissionColumn.validateJsonObject(jsonObj.getAsJsonObject("mySubmission"));
      }
      // validate the optional field `submissionRange`
      if (jsonObj.getAsJsonObject("submissionRange") != null) {
        TitaniumSubmissionRangeColumn.validateJsonObject(jsonObj.getAsJsonObject("submissionRange"));
      }
      // validate the optional field `submissionStatisticalBoundaries`
      if (jsonObj.getAsJsonObject("submissionStatisticalBoundaries") != null) {
        TitaniumSubmissionStatisticsColumn.validateJsonObject(jsonObj.getAsJsonObject("submissionStatisticalBoundaries"));
      }
      // validate the optional field `tradeTimeSeries`
      if (jsonObj.getAsJsonObject("tradeTimeSeries") != null) {
        TitaniumAvailableTrades.validateJsonObject(jsonObj.getAsJsonObject("tradeTimeSeries"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumComparisonTable.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumComparisonTable' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumComparisonTable> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumComparisonTable.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumComparisonTable>() {
           @Override
           public void write(JsonWriter out, TitaniumComparisonTable value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumComparisonTable read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumComparisonTable given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumComparisonTable
  * @throws IOException if the JSON string is invalid with respect to TitaniumComparisonTable
  */
  public static TitaniumComparisonTable fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumComparisonTable.class);
  }

 /**
  * Convert an instance of TitaniumComparisonTable to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

